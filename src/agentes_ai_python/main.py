"example_agents_crewai_env\Scripts\activate"

import os
from crewai import Crew, Process
from crew import configure_crew
from config_loader import load_agents, load_tasks

def main():
    # Cargar configuración de agentes y tareas
    agents = load_agents("src/agentes_ai_python/config/agents.yaml")
    tasks = load_tasks("src/agentes_ai_python/config/tasks.yaml")

    # Configurar el equipo de agentes y ejecutar el flujo de trabajo
    crew = configure_crew(agents, tasks, Process.SEQUENTIAL)
    result = crew.kickoff(inputs={"topic": "Python"})
    print(result)

if __name__ == "__main__":
    main()
