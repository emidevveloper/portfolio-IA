import google.generativeai as genai
import os

# Configuración de Gemini usando el Secret de GitHub
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

# Ajustado a "styles.css" según tu captura de pantalla
archivo_objetivo = "styles.css"

# 1. Leer el código actual
if os.path.exists(archivo_objetivo):
    with open(archivo_objetivo, "r") as f:
        css_actual = f.read()
else:
    css_actual = "/* Estilo base creado por Gemini */"

# 2. El Prompt creativo
prompt = f"""
Eres un diseñador web noctámbulo. Tu misión es añadir al final de este CSS 
una sección de estilos experimentales (colores neón, animaciones o efectos hover).
No borres nada, solo añade tu toque al final. Nada de animaciones con efectos de flashes o estroboscópicos
CÓDIGO ACTUAL:
{css_actual}
"""

# 3. Generación
try:
    response = model.generate_content(prompt)
    nuevo_contenido = response.text
    
    # Limpiar formato markdown si la IA lo incluye
    nuevo_contenido = nuevo_contenido.replace("```css", "").replace("```", "")

    # 4. Sobreescribir el archivo
    with open(archivo_objetivo, "w") as f:
        f.write(nuevo_contenido)
    print("CSS actualizado con éxito.")
except Exception as e:
    print(f"Error: {e}")