import sys
from agentes_ai_python.crew import EducationalContentCrew

def run(topic="Python"):
    """Ejecuta el flujo de trabajo de generación de contenido educativo sobre un tema específico y devuelve el resultado."""
    inputs = {
        'topic': topic
    }
    # Captura el resultado de kickoff
    result = EducationalContentCrew().crew().kickoff(inputs=inputs)
    return result  # Asegúrate de devolver el resultado

def train():
    """Entrena el crew de generación de contenido educativo por un número específico de iteraciones."""
    inputs = {
        'topic': "Python"
    }
    try:
        n_iterations = int(sys.argv[1]) if len(sys.argv) > 1 else 1
        EducationalContentCrew().crew().train(n_iterations=n_iterations, inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        train()
    else:
        run("Python")  # Puedes cambiar el tema a investigar aquí
