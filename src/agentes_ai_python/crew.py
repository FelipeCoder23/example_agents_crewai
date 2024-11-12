from typing import List
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Importación de herramientas de CrewAI
from crewai_tools import YoutubeChannelSearchTool, YoutubeVideoSearchTool
from pydantic import BaseModel

# Definir las herramientas
youtube_channel_tool = YoutubeChannelSearchTool()
youtube_video_tool = YoutubeVideoSearchTool()

@CrewBase
class EducationalContentCrew:
    """Crew para generación de contenido educativo sobre temas específicos en Python"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def investigador_tendencias(self) -> Agent:
        return Agent(
            config=self.agents_config['investigador_tendencias'],
            tools=[youtube_channel_tool, youtube_video_tool],
            verbose=True
        )
    
    @agent
    def guionista_contenidos(self) -> Agent:
        return Agent(
            config=self.agents_config['guionista_contenidos'],
            verbose=True
        )
    
    @agent
    def revisor_contenidos(self) -> Agent:
        return Agent(
            config=self.agents_config['revisor_contenidos'],
            verbose=True
        )
    
    @task
    def investigacion_tema(self) -> Task:
        return Task(
            config=self.tasks_config['investigacion_tema'],
            agent=self.investigador_tendencias()
        )

    @task
    def creacion_guion(self) -> Task:
        return Task(
            config=self.tasks_config['creacion_guion'],
            agent=self.guionista_contenidos()
        )

    @task
    def revision_guion(self) -> Task:
        return Task(
            config=self.tasks_config['revision_guion'],
            agent=self.revisor_contenidos()
        )

    @crew
    def crew(self) -> Crew:
        """Crea el crew de generación de contenido educativo"""
        return Crew(
            agents=self.agents,  # Agentes creados automáticamente por el decorador @agent
            tasks=self.tasks,  # Tareas creadas automáticamente por el decorador @task
            process=Process.sequential,
            verbose=2,
        )
