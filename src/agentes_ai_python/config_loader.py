import yaml

def load_agents(filepath):
    with open(filepath, 'r') as file:
        agents = yaml.safe_load(file)
    if not isinstance(agents, dict):
        raise ValueError("La configuración de agentes no es un diccionario.")
    return agents

def load_tasks(filepath):
    with open(filepath, 'r') as file:
        tasks = yaml.safe_load(file)
    if not isinstance(tasks, dict):
        raise ValueError("La configuración de tareas no es un diccionario.")
    return tasks
