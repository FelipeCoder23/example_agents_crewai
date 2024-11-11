# Esta sección utiliza las herramientas integradas de YouTube de CrewAI, sin crear herramientas adicionales

from crewai_tools import YoutubeChannelSearchTool, YoutubeVideoSearchTool

# Instanciar las herramientas disponibles para su uso
youtube_channel_search_tool = YoutubeChannelSearchTool()
youtube_video_search_tool = YoutubeVideoSearchTool()
