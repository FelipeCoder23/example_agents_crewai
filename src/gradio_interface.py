import gradio as gr
from agentes_ai_python.main import run

def run_agent_pipeline(topic):
    """Ejecuta el flujo de generación de contenido educativo y muestra el resultado."""
    result = run(topic=topic)
    output_text = f"**Tema Investigado**: {topic}\n\n{result}"
    return output_text

# CSS actualizado con tamaños ajustados
css = """
body {
    background-color: #13151a !important;
}
.container {
    max-width: 900px;
    margin: auto;
    padding: 15px;
}
.header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 25px;
    border-radius: 12px;
    margin-bottom: 25px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}
.title {
    text-align: center;
    color: white;
    font-size: 2em;
    margin-bottom: 0.3em;
}
.subtitle {
    text-align: center;
    color: rgba(255, 255, 255, 0.9);
    font-size: 1em;
    margin-bottom: 0.5em;
}
.features {
    background: #1e2028;
    padding: 20px;
    border-radius: 8px;
    margin-bottom: 20px;
}
.features-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 15px;
    margin-top: 15px;
}
.feature-card {
    background: #282a36;
    padding: 15px;
    border-radius: 6px;
    text-align: center;
    border: 1px solid rgba(255, 255, 255, 0.1);
}
.feature-card h4 {
    font-size: 1.5em;
    margin: 0;
    margin-bottom: 8px;
}
.feature-card p {
    margin: 0;
    font-size: 0.9em;
    color: rgba(255, 255, 255, 0.9);
}
.input-section {
    background: #1e2028;
    padding: 20px;
    border-radius: 8px;
    margin-bottom: 20px;
}
.output-container {
    background: #282a36;
    padding: 20px;
    border-radius: 8px;
    margin-top: 15px;
    border: 1px solid rgba(255, 255, 255, 0.1);
}
.generate-button {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    border: none !important;
    color: white !important;
    padding: 10px 20px !important;
    border-radius: 6px !important;
    font-weight: bold !important;
    font-size: 0.9em !important;
}
.examples-section, .tips-section {
    background: #1e2028;
    padding: 20px;
    border-radius: 8px;
    margin-top: 15px;
    font-size: 0.9em;
}
"""

# Interfaz mejorada y simplificada
with gr.Blocks(css=css, theme=gr.themes.Soft()) as iface:
    with gr.Column(elem_classes="container"):
        with gr.Column(elem_classes="header"):
            gr.Markdown("# 🤖 Generador de Contenido Educativo con IA")
            gr.Markdown("Transforma cualquier tema en contenido educativo estructurado y profesional")
        
        with gr.Column(elem_classes="features"):
            gr.Markdown("### ✨ Características del Contenido")
            with gr.Column(elem_classes="features-grid"):
                for icon, text in [
                    ("📝", "Introducción Clara"),
                    ("🎯", "Conceptos Clave"),
                    ("💡", "Ejemplos Prácticos"),
                    ("🔨", "Ejercicios Aplicados")
                ]:
                    with gr.Column(elem_classes="feature-card"):
                        gr.Markdown(f"#### {icon}\n{text}")
        
        with gr.Column(elem_classes="input-section"):
            topic_input = gr.Textbox(
                label="🔍 ¿Sobre qué tema quieres aprender hoy?",
                placeholder="Ejemplo: Conceptos básicos de POO en Python"
            )
            submit_button = gr.Button(
                "🚀 Generar",
                elem_classes="generate-button"
            )
            
            output_text = gr.Markdown(
                label="📖 Tu Contenido Educativo",
                elem_classes="output-container"
            )

        # Examples Section
        with gr.Column(elem_classes="examples-section"):
            gr.Markdown("### 📚 Ejemplos Populares")
            gr.Examples(
                examples=[
                    ["Conceptos básicos de Programación Orientada a Objetos en Python"],
                    ["Automatización de tareas con Python"],
                    ["Análisis de datos con Python y Pandas"],
                    ["Visualización de datos con Matplotlib"],
                    ["Web Scraping con Beautiful Soup"],
                    ["APIs RESTful con FastAPI"],
                ],
                inputs=topic_input
            )

        # Tips Section
        with gr.Column(elem_classes="tips-section"):
            gr.Markdown("""
            ### 💡 Consejos para Mejores Resultados
            
            <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px;'>
                <div>
                    <h4>🎯 Sé Específico</h4>
                    <p>Cuanto más específico sea tu tema, mejores serán los resultados</p>
                </div>
                <div>
                    <h4>⏱️ Ten Paciencia</h4>
                    <p>El proceso puede tomar unos minutos para generar contenido de calidad</p>
                </div>
                <div>
                    <h4>📋 Explora Ejemplos</h4>
                    <p>Revisa los ejemplos para inspirarte</p>
                </div>
            </div>
            """)

    submit_button.click(
        fn=run_agent_pipeline,
        inputs=topic_input,
        outputs=output_text
    )

if __name__ == "__main__":
    iface.launch(
        server_name="0.0.0.0",
        server_port=7860
    )
