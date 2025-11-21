import re
from pathlib import Path

from hatchling.builders.hooks.plugin.interface import BuildHookInterface
from grpc_tools import protoc


class CustomBuildHook(BuildHookInterface):
    def initialize(self, version: str, build_data: dict):
        file_names = "request.proto", "struct.proto", "response.proto"

        for file_name in file_names:
            protoc.main([
                "grpc_tools.protoc",
                "--proto_path=balethon/proto/definitions",
                "--python_out=balethon/proto",
                "--pyi_out=balethon/proto",
                "--grpc_python_out=balethon/proto",
                f"balethon/proto/definitions/{file_name}"
            ])

        proto_dir = Path("balethon/proto")
        for file in proto_dir.glob("*_pb2*.py"):
            content = file.read_text()
            content = re.sub(
                r'^import (\w+_pb2)',
                r'from balethon.proto import \1',
                content,
                flags=re.MULTILINE
            )
            file.write_text(content)
