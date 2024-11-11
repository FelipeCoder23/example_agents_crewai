import os
from dotenv import load_dotenv
from crewai import Agent, Crew, Process
from crewai_tools import YoutubeChannelSearchTool, YoutubeVideoSearchTool

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

def configure_crew(agents, tasks, process_type):
    # Crear instancia de Agent para el investigador con herramientas de YouTube
    investigador = Agent(
        role=agents["investigador_tendencias"]["role"],
        goal=agents["investigador_tendencias"]["goal"],
        tools=[YoutubeChannelSearchTool(), YoutubeVideoSearchTool()],
        backstory=agents["investigador_tendencias"]["backstory"]
    )

    # Crear instancia de Agent para el guionista
    guionista = Agent(
        role=agents["guionista_contenidos"]["role"],
        goal=agents["guionista_contenidos"]["goal"],
        backstory=agents["guionista_contenidos"]["backstory"]
    )

    # Configurar las tareas y asignar agentes
    investigacion_tema_task = {
        **tasks["investigacion_tema"],
        "agent": investigador  # Asigna el agente investigador
    }

    creacion_guion_task = {
        **tasks["creacion_guion"],
        "agent": guionista  # Asigna el agente guionista
    }

    # Configurar Crew con el proceso secuencial
    crew = Crew(
        agents=[investigador, guionista],
        tasks=[investigacion_tema_task, creacion_guion_task],
        process=process_type
    )

    return crew
