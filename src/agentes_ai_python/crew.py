from crewai import Agent, Task, Crew, Process
from crewai_tools import YoutubeChannelSearchTool, YoutubeVideoSearchTool

def configure_crew(agents, tasks, process_type):
    # Instancia las herramientas
    channel_search_tool = YoutubeChannelSearchTool()
    video_search_tool = YoutubeVideoSearchTool()
    
    # Crear instancias de agentes y mapearlas con nombres
    agents_instances = {}
    for agent_name, agent_config in agents.items():
        # Asignación de herramientas específicas
        if agent_name == "investigador_tendencias":
            agent_config["tools"] = [channel_search_tool, video_search_tool]
        agent_instance = Agent(**agent_config)
        agents_instances[agent_name] = agent_instance  # Mapea con el nombre exacto del agente
    
    # Crear instancias de tareas y asociarlas con sus agentes
    tasks_instances = []
    for task_name, task_config in tasks.items():
        agent_name = task_config.get("agent")  # Obtener el nombre del agente desde la tarea
        agent_instance = agents_instances.get(agent_name)  # Buscar el agente por su nombre exacto
        if agent_instance is None:
            raise ValueError(f"No se encontró el agente '{agent_name}' para la tarea '{task_name}'")

        task_instance = Task(
            description=task_config["description"],
            expected_output=task_config["expected_output"],
            agent=agent_instance  # Asocia la instancia del agente aquí
        )
        tasks_instances.append(task_instance)

    # Configura y retorna la tripulación (Crew)
    crew = Crew(agents=list(agents_instances.values()), tasks=tasks_instances, process=process_type)
    return crew
