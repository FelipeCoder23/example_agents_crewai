# Proyecto: Generador de Contenido Educativo con CrewAI

## Descripción General
Este proyecto utiliza **CrewAI** para orquestar agentes AI autónomos que colaboran en la creación de contenido educativo estructurado. Los agentes trabajan en conjunto para investigar, redactar y revisar un guion educativo sobre un tema específico. Este ejemplo demuestra el potencial de CrewAI para implementar flujos complejos de trabajo con agentes especializados.


## Agentes
### **1. Investigador de Tendencias**
- **Rol:** Buscar contenido relevante en YouTube relacionado con el tema solicitado.
- **Tasks:**
  - Realizar búsquedas iniciales para identificar contenido general.
  - Analizar canales relevantes para extraer videos específicos.
- **Herramientas:**
  - `Search a YouTube Video Content`
  - `Search a YouTube Channel Content`

### **2. Guionista de Contenidos**
- **Rol:** Crear un guion educativo estructurado y claro basado en la información recopilada.
- **Tasks:**
  - Redactar introducción, conceptos clave, ejemplos prácticos, aplicaciones reales y ejercicios.
- **Herramientas:**  
  - No requiere herramientas adicionales.

### **3. Revisor de Contenidos**
- **Rol:** Revisar y mejorar el guion para garantizar claridad, coherencia y precisión técnica.
- **Tasks:**
  - Identificar errores o áreas de mejora.
  - Asegurar que el contenido sea adecuado para el público objetivo.
- **Herramientas:**  
  - No requiere herramientas adicionales.

## Configuración
1. Clona este repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_PROYECTO>

2. Instala las dependencias necesarias:

pip install -r requirements.txt

3. Configura tus claves API, en este caso se utilizo el modelo de OpenAI gtp 3.5