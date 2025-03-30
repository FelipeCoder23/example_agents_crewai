import yaml

def load_agents(filepath):
    """
    Carga la configuración de agentes desde un archivo YAML.
    
    Args:
        filepath: Ruta al archivo YAML de configuración de agentes
    
    Returns:
        Un diccionario con la configuración de agentes
    
    Raises:
        ValueError: Si la configuración no es un diccionario
    """
    with open(filepath, 'r') as file:
        agents = yaml.safe_load(file)
    if not isinstance(agents, dict):
        raise ValueError("La configuración de agentes no es un diccionario.")
    return agents

def load_tasks(filepath):
    """
    Carga la configuración de tareas desde un archivo YAML.
    
    Args:
        filepath: Ruta al archivo YAML de configuración de tareas
    
    Returns:
        Un diccionario con la configuración de tareas
    
    Raises:
        ValueError: Si la configuración no es un diccionario
    """
    with open(filepath, 'r') as file:
        tasks = yaml.safe_load(file)
    if not isinstance(tasks, dict):
        raise ValueError("La configuración de tareas no es un diccionario.")
    return tasks
