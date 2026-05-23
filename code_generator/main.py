import re
from pathlib import Path

from grpc_tools import protoc


def compile_proto_files(directory: Path = Path("proto"), main_package: bool = True):
    for child in directory.iterdir():
        if child.is_dir():
            compile_proto_files(child, main_package=False)
            continue

        path = child.name if main_package else f"{child.parent.name}/{child.name}"
        protoc.main([
            "grpc_tools.protoc",
            "--proto_path=proto",
            "--python_out=../balethon/proto",
            "--pyi_out=../balethon/proto",
            "--grpc_python_out=../balethon/proto",
            f"proto/{path}"
        ])


def fix_compiled_files(directory: Path = Path("../balethon/proto"), main_package: bool = True):
    init_file = create_init_file(directory)

    for child in directory.iterdir():
        if child.name.startswith("_"):
            continue

        if child.is_dir():
            fix_compiled_files(child, main_package=False)
            continue

        if child.name.endswith("_pb2.py") or child.name.endswith("_pb2.pyi"):
            fix_compiled_file_imports(child, main_package)

        if child.name.endswith("_pb2.py"):
            add_import_to_init(init_file, child, main_package)


def fix_compiled_file_imports(file: Path, main_package: bool = False):
    dots = "." if main_package else ".."

    content = file.read_text(encoding="utf-8")
    content = re.sub(
        r"^(from\s+)(\w+)(\s+import\s+.*pb2.*)$",
        fr"\1{dots}\2\3",
        content,
        flags=re.MULTILINE
    )
    content = re.sub(
        r"^(import\s+.*_pb2.*)",
        fr"from {dots} \1",
        content,
        flags=re.MULTILINE
    )
    file.write_text(content, encoding="utf-8")


def create_init_file(directory: Path) -> Path:
    init_file = directory / "__init__.py"
    init_file.write_text("", encoding="utf-8")
    return init_file


def add_import_to_init(init_file: Path, file: Path, main_package: bool = False):
    content = init_file.read_text(encoding="utf-8")
    name = file.name.split(".")[0]
    if main_package:
        alias = name.replace("_pb2", "")
        content += f"from . import {name} as {alias}\n"
    else:
        content += f"from .{name} import *\n"
    init_file.write_text(content, encoding="utf-8")


def generate_parameters_for_requests():
    proto_dir = Path("proto", "requests")
    init_file = Path("..", "balethon", "proto", "requests", "__init__.py")

    init_content = init_file.read_text(encoding="utf-8")

    for file in proto_dir.glob("*.proto"):
        proto_content = file.read_text(encoding="utf-8")

        service_name = re.search(r"// Service name: (.+)", proto_content).group(1)

        classes = re.findall(r"^message (\w+)", proto_content, flags=re.MULTILINE)

        results = re.finditer(
            r"^// Method: ([^\n]+)\n"
            r"(?:^//[^\n]*\n)*"
            r"message (\w+)",
            proto_content,
            flags=re.MULTILINE
        )
        methods = {m.group(2): m.group(1) for m in results}

        results = re.finditer(
            r"^// HTTP2\n"
            r"(?:^//[^\n]*\n)*"
            r"message (\w+)",
            proto_content,
            flags=re.MULTILINE
        )
        http2_classes = [m.group(1) for m in results]

        for cls in classes:
            init_content += "\n"
            init_content += f"{cls}.service_name = \"{service_name}\"\n"
            method_name = methods.get(cls, cls)
            init_content += f"{cls}.method = \"{method_name}\"\n"
            is_http2 = cls in http2_classes
            init_content += f"{cls}.http2 = {is_http2}\n"

    init_file.write_text(init_content, encoding="utf-8")


def main():
    compile_proto_files()

    fix_compiled_files()

    generate_parameters_for_requests()


if __name__ == "__main__":
    main()
