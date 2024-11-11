import yaml

def load_agents(filepath):
    with open(filepath, "r") as file:
        return yaml.safe_load(file)

def load_tasks(filepath):
    with open(filepath, "r") as file:
        return yaml.safe_load(file)
