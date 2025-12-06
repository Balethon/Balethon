import re
from pathlib import Path

from grpc_tools import protoc


def main():
    file_names = "request.proto", "struct.proto", "response.proto"

    for file_name in file_names:
        protoc.main([
            "grpc_tools.protoc",
            "--proto_path=proto",
            "--python_out=../balethon/proto",
            "--pyi_out=../balethon/proto",
            "--grpc_python_out=../balethon/proto",
            f"proto/{file_name}"
        ])

    proto_dir = Path("../balethon/proto")
    for file in proto_dir.glob("*_pb2*.py"):
        content = file.read_text()
        content = re.sub(
            r'^import (\w+_pb2)',
            r'from balethon.proto import \1',
            content,
            flags=re.MULTILINE
        )
        file.write_text(content)


if __name__ == "__main__":
    main()
