from crewai import Crew, Process
from crewai_tools import YoutubeChannelSearchTool, YoutubeVideoSearchTool

def configure_crew(agents, tasks, process_type):
    # Instancia y asigna herramientas a los agentes
    investigador = agents["investigador_tendencias"]
    investigador.tools = [YoutubeChannelSearchTool(), YoutubeVideoSearchTool()]

    guionista = agents["guionista_contenidos"]

    # Configurar Crew con el proceso secuencial
    crew = Crew(
        agents=[investigador, guionista],
        tasks=[tasks["investigacion_tema"], tasks["creacion_guion"]],
        process=process_type
    )
    return crew
