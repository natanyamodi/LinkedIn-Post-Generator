import yaml

def load_config(filepath="config/config.yaml"):
    with open(filepath, "r") as file:
        config = yaml.safe_load(file)

    return config


def get_api_key(key_name):
    config = load_config()
    return config.get(key_name)