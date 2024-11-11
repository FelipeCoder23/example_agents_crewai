"example_agents_crewai_env\Scripts\activate"

import os
from dotenv import load_dotenv  # Importar dotenv para cargar variables de entorno
from crewai import Crew, Process
from agentes_ai_python.crew import configure_crew
from agentes_ai_python.config_loader import load_agents, load_tasks

# Cargar las variables de entorno desde el archivo .env
load_dotenv()
print("API Key:", os.getenv("OPENAI_API_KEY"))

def main():
    # Cargar configuración de agentes y tareas
    agents = load_agents("agentes_ai_python/config/agents.yaml")
    tasks = load_tasks("agentes_ai_python/config/tasks.yaml")

    # Configurar el equipo de agentes y ejecutar el flujo de trabajo
    crew = configure_crew(agents, tasks, Process.sequential)
    result = crew.kickoff(inputs={"topic": "Python"})
    return result

if __name__ == "__main__":
    main()
