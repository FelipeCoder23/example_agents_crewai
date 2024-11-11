import gradio as gr
from main import main

def run_agent_pipeline(topic):
    # Ejecuta la pipeline de agentes con el tema dado y muestra el resultado
    result = main()
    return f"Tema Investigado: {topic}\n\nResultado:\n{result}"

iface = gr.Interface(
    fn=run_agent_pipeline,
    inputs="text",
    outputs="text",
    title="Generador de Contenido Educativo sobre Python",
    description="Ingrese un tema para iniciar el proceso de investigación y generación de contenido."
)

if __name__ == "__main__":
    iface.launch()
