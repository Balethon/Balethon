from hatchling.builders.hooks.plugin.interface import BuildHookInterface
from grpc_tools import protoc


class CustomBuildHook(BuildHookInterface):
    def initialize(self, version: str, build_data: dict):
        filenames = "request.proto", "struct.proto", "response.proto"

        for filename in filenames:
            command = [
                "grpc_tools.protoc",
                "--proto_path=balethon/proto/definitions",
                "--python_out=balethon/proto",
                "--pyi_out=balethon/proto",
                "--grpc_python_out=balethon/proto",
                f"balethon/proto/definitions/{filename}"
            ]
            protoc.main(command)
