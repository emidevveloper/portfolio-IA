import google.generativeai as genai
import os
from datetime import datetime

# Configuración de Gemini usando el Secret de GitHub
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

# Archivo objetivo
archivo_objetivo = "styles.css"

# 1. Leer el código actual
if os.path.exists(archivo_objetivo):
    with open(archivo_objetivo, "r") as f:
        css_actual = f.read()
else:
    css_actual = "/* Estilo base creado por Gemini */"

# 2. El Prompt con tus nuevas restricciones
prompt = f"""
Eres un diseñador web experto. Tu misión es añadir al final de este CSS 
una sección de estilos experimentales (colores neón o efectos hover elegantes).

REGLAS DE SEGURIDAD:
- Prohibido usar animaciones con efectos de flashes, parpadeos rápidos o estroboscópicos.
- Los efectos deben ser suaves y seguros para personas con fotosensibilidad.
- No borres el código anterior, solo añade al final.

CÓDIGO ACTUAL:
{css_actual}
"""

# 3. Generación y limpieza
try:
    response = model.generate_content(prompt)
    nuevo_contenido = response.text
    nuevo_contenido = nuevo_contenido.replace("```css", "").replace("```", "").strip()

    # 4. Forzar cambio con marca de tiempo (Evita el error de 'nothing to commit')
    timestamp = f"\n\n/* Actualizado por Gemini: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} */\n"

    # 5. Sobreescribir el archivo completo
    with open(archivo_objetivo, "w") as f:
        f.write(css_actual + "\n" + nuevo_contenido + timestamp)
    
    print("CSS actualizado con éxito.")
except Exception as e:
    print(f"Error: {e}")
