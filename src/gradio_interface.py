import gradio as gr
from agentes_ai_python.main import main

def run_agent_pipeline(topic):
    # Ejecuta la función main y captura el resultado
    result = main()  # Asegúrate de que main() retorna un valor que Gradio pueda capturar
    # Formatea el resultado para mostrarlo en la interfaz de Gradio
    output_text = f"Tema Investigado: {topic}\n\nResultado:\n{result}"
    return output_text

iface = gr.Interface(
    fn=run_agent_pipeline,
    inputs="text",
    outputs="text",
    title="Generador de Contenido Educativo sobre Python",
    description="Ingrese un tema para iniciar el proceso de investigación y generación de contenido."
)

if __name__ == "__main__":
    iface.launch()
