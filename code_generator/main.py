import re
from pathlib import Path

from grpc_tools import protoc


def compile_proto_files():
    proto_dir = Path("proto")

    for child in proto_dir.iterdir():
        if child.is_dir():
            for file in child.glob("*.proto"):
                protoc.main([
                    "grpc_tools.protoc",
                    "--proto_path=proto",
                    "--python_out=../balethon/proto",
                    "--pyi_out=../balethon/proto",
                    "--grpc_python_out=../balethon/proto",
                    f"proto/{file.parent.name}/{file.name}"
                ])
        else:
            protoc.main([
                "grpc_tools.protoc",
                "--proto_path=proto",
                "--python_out=../balethon/proto",
                "--pyi_out=../balethon/proto",
                "--grpc_python_out=../balethon/proto",
                f"proto/{child.name}"
            ])


def fix_compiled_files():
    proto_dir = Path("../balethon/proto")

    main_init_file = create_init_file(proto_dir)

    for child in proto_dir.iterdir():
        if child.name.startswith("_"):
            continue

        if child.is_file():
            if child.name.endswith("_pb2.py") or child.name.endswith("_pb2.pyi"):
                fix_compiled_file_imports(child, main_package=True)

            if child.name.endswith("_pb2.py"):
                add_import_to_main_init(main_init_file, child)

            continue

        init_file = create_init_file(child)

        for file in child.iterdir():
            if file.name.endswith("_pb2.py") or file.name.endswith("_pb2.pyi"):
                fix_compiled_file_imports(file)

            if file.name.endswith("_pb2.py"):
                add_import_to_init(init_file, file)


def fix_compiled_file_imports(file, main_package=False):
    if main_package:
        dots = "."
    else:
        dots = ".."

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


def create_init_file(directory):
    init_file = directory / "__init__.py"
    init_file.write_text("", encoding="utf-8")
    return init_file


def add_import_to_main_init(init_file, file):
    content = init_file.read_text(encoding="utf-8")
    name = file.name.split(".")[0]
    alias = name.replace("_pb2", "")
    content += f"from . import {name} as {alias}\n"
    init_file.write_text(content, encoding="utf-8")


def add_import_to_init(init_file, file):
    content = init_file.read_text(encoding="utf-8")
    name = file.name.split(".")[0]
    content += f"from .{name} import *\n"
    init_file.write_text(content, encoding="utf-8")


def main():
    compile_proto_files()

    fix_compiled_files()


if __name__ == "__main__":
    main()
