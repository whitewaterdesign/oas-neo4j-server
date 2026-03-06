from app.yaml_client import get_yaml_str, yaml_to_dict
from app.service.build_graph import create_graph
from app.service.db import driver

yaml_str = get_yaml_str()
yaml_dict = yaml_to_dict(yaml_str)


if __name__ == "__main__":
    create_graph(driver, yaml_dict)
