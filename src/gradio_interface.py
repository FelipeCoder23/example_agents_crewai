import gradio as gr
from agentes_ai_python.main import run

def run_agent_pipeline(topic):
    """Ejecuta el flujo de generación de contenido educativo y muestra el resultado."""
    # Ejecuta la función run con el tema proporcionado
    result = run(topic=topic)  # Pasa el tema proporcionado a la función main

    # Formatea el resultado para mostrarlo en la interfaz de Gradio
    output_text = f"**Tema Investigado**: {topic}\n\n{result}"
    return output_text

# Configuración de la interfaz en formato de columna y con un estilo de carga visible
with gr.Blocks() as iface:
    gr.Markdown("# Generador de Contenido Educativo sobre Python")
    gr.Markdown("Ingrese un tema para iniciar el proceso de investigación y generación de contenido educativo. El guion incluirá una introducción, conceptos clave, aplicaciones prácticas y un ejercicio de programación.")
    
    # Entrada de texto para el tema en una columna separada
    topic_input = gr.Textbox(label="Ingrese un tema", placeholder="Ejemplo: Conceptos básicos de Programación Orientada a Objetos en Python")
    
    # Área de salida para mostrar el texto del guion generado
    output_text = gr.Markdown(label="Guion Educativo Generado")

    # Botón para ejecutar el pipeline
    submit_button = gr.Button("Generar Contenido")

    # Configuración para ejecutar la función con el botón y mostrar el estado de "cargando"
    submit_button.click(fn=run_agent_pipeline, inputs=topic_input, outputs=output_text)
    
    # Ejemplos de temas a elegir
    gr.Examples(
        examples=[
            ["Conceptos básicos de Programación Orientada a Objetos en Python"],
            ["Automatización de tareas con Python"],
            ["Análisis de datos en Python con Pandas"],
            ["Visualización de datos con Matplotlib"],
        ],
        inputs=topic_input
    )

if __name__ == "__main__":
    iface.launch()
