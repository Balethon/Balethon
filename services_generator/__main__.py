from json import load
from os import mkdir
from os.path import join
# 278, 240, 130, 70
service_file_template = """
class {pascal_case}:

    async def {snake_case}(
            {arguments}
    ){return_type}:
        data = {data}
        return await self.execute("{method}", "{camel_case}", **data)
""".strip()

init_file_template = """
class {pascal_case}(
    {classes}
):
    pass
""".strip()


def pascal_case(string):
    words = string.split("_")
    words = [word.capitalize() for word in words]
    return "".join(words)


def camel_case(string):
    words = string.split("_")
    words = [word.capitalize() if i > 0 else word for i, word in enumerate(words)]
    return "".join(words)


def load_services():
    with open("services.json", encoding="utf-8") as services_json:
        return load(services_json)


def resolve_imports(service_data):
    types = ["balethon.Client"]
    if service_data.get("arguments"):
        for argument_data in service_data["arguments"].values():
            if argument_data.get("types"):
                if len(argument_data["types"]) > 1:
                    types.append("typing.Union")
                types.extend(argument_data["types"])
    if service_data.get("return_type"):
        types.append(service_data["return_type"])
    imports = {}
    for type in types:
        if "." in type:
            destination, obj = type.rsplit(".", maxsplit=1)
            if destination in imports:
                if obj in imports[destination]:
                    continue
                imports[destination].append(obj)
            else:
                imports[destination] = [obj]
    imports_list = []
    for destination, objects in imports.items():
        objects_string = ", ".join(objects)
        imports_list.append(f"from {destination} import {objects_string}")
    return "\n".join(imports_list)


def format_argument(argument_name, argument_data):
    argument_string = argument_name
    if argument_data.get("types"):
        types = [type.split(".")[-1] for type in argument_data["types"].copy()]
        if len(types) > 1:
            argument_string = f"{argument_string}: Union[{', '.join(types)}]"
        else:
            argument_string = f"{argument_string}: {types[0]}"
    return argument_string


def create_service_file(package, service_name, service_data):
    imports = resolve_imports(service_data)

    service_arguments = {"self": {"types": ["balethon.Client"]}}
    if service_data.get("arguments"):
        service_arguments.update(service_data["arguments"])
    arguments = (",\n" + " "*12).join(format_argument(name, data) for name, data in service_arguments.items())

    with open(join(package, f"{service_name}.py"), "w") as file:
        service_class = service_file_template.format(
            pascal_case=pascal_case(service_name),
            snake_case=service_name,
            arguments=arguments,
            return_type="" if service_data.get("return_type") is None else f" -> {service_data['return_type'].split('.')[-1]}",
            data="{}",
            method=service_data["method"],
            camel_case=camel_case(service_name)
        )
        if imports:
            file_data = f"{imports}\n\n\n{service_class}"
        else:
            file_data = service_class
        file.write(file_data + "\n")


def create_init_file(package, services):
    imports = "\n".join(f"from .{name} import {pascal_case(name)}" for name in services)

    with open(join(package, "__init__.py"), "w") as file:
        package_class = init_file_template.format(
            pascal_case=pascal_case(package),
            classes=(",\n" + " "*4).join(pascal_case(name) for name in services)
        )
        file_data = f"{imports}\n\n\n{package_class}"
        file.write(file_data + "\n")


def main():
    all_services = load_services()

    for package, services in all_services.items():
        try:
            mkdir(package)
        except FileExistsError:
            pass
        for name, data in services.items():
            create_service_file(package, name, data)
        create_init_file(package, services)


if __name__ == "__main__":
    main()
