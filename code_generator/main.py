import re
from pathlib import Path

from grpc_tools import protoc


def compile_proto_files():
    proto_dir = Path("proto")

    for sub_dir in proto_dir.iterdir():
        for file in sub_dir.glob("*.proto"):
            protoc.main([
                "grpc_tools.protoc",
                "--proto_path=proto",
                "--python_out=../balethon/proto",
                "--pyi_out=../balethon/proto",
                "--grpc_python_out=../balethon/proto",
                f"proto/{file.parent.name}/{file.name}"
            ])


def fix_compiled_files():
    proto_dir = Path("../balethon/proto")

    for sub_dir in proto_dir.iterdir():
        if not sub_dir.is_dir():
            continue

        if sub_dir.name.startswith("_"):
            continue

        init_file = create_init_file(sub_dir)

        for file in sub_dir.glob("*_pb2*.py"):
            fix_compiled_file_imports(file)
            if file.name.endswith("_pb2.py"):
                add_imports_to_init(init_file, file)


def fix_compiled_file_imports(file):
    content = file.read_text()
    content = re.sub(
        r"^(from\s+)(\w+)(\s+import\s+.*pb2.*)$",
        r"\1..\2\3",
        content,
        flags=re.MULTILINE
    )
    file.write_text(content)


def create_init_file(directory):
    init_file = directory / "__init__.py"
    init_file.write_text("")
    return init_file


def add_imports_to_init(init_file, file):
    content = init_file.read_text()
    name = file.name.split(".")[0]
    content += f"from .{name} import *\n"
    init_file.write_text(content)


def main():
    compile_proto_files()

    fix_compiled_files()


if __name__ == "__main__":
    main()
