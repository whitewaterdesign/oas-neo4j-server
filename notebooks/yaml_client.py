import os
import yaml
from typing import Any



def get_yaml_str(file_path: str = "../data/example.spec.yaml") -> str:
    """
    Gets the contents of a YAML file in file path relative to current file
    :param file_path: str
    :return: str - contents of the YAML file
    """
    base_path = os.path.dirname(__file__)
    absolute_path = os.path.normpath(os.path.join(base_path, file_path))
    with open(absolute_path, 'r') as file:
        return file.read()


def yaml_to_dict(yaml_str: str) -> dict[str, Any]:
    """
    Converts a YAML string to an EvergreenYamlInput dictionary
    :param yaml_str: str - YAML string
    :return: EvergreenYamlInput
    """
    return yaml.safe_load(yaml_str)
