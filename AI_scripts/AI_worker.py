import google.generativeai as genai
import os
from datetime import datetime

# 1. Configuración de Gemini
# Usamos el nombre del modelo más estable para evitar errores 404
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-3-flash-preview')

# 2. Archivo objetivo (asegúrate de que el nombre sea exacto)
archivo_objetivo = "styles.css"

# 3. Leer el código actual para dárselo a la IA
if os.path.exists(archivo_objetivo):
    with open(archivo_objetivo, "r") as f:
        css_actual = f.read()
else:
    css_actual = "/* Estilo base inicial */"

# 4. Prompt con tus restricciones de seguridad visual
prompt = f"""
Eres un diseñador web experto en interfaces modernas. 
Tu misión es añadir al final de este código CSS una sección de estilos experimentales.

REGLAS ESTRICTAS:
- PROHIBIDO: No uses animaciones con flashes, parpadeos rápidos o efectos estroboscópicos.
- SEGURIDAD: Los efectos deben ser suaves (glows lentos, hovers elegantes, colores neón fijos).
- No borres nada del código original, solo añade al final.
- Devuelve SOLO el código CSS, sin explicaciones.

CÓDIGO ACTUAL:
{css_actual}
"""

# 5. Ejecución y guardado
try:
    print("Despertando a la IA...")
    response = model.generate_content(prompt)
    nuevo_contenido = response.text
    
    # Limpiamos posibles etiquetas de Markdown que la IA a veces añade
    nuevo_contenido = nuevo_contenido.replace("```css", "").replace("```", "").strip()

    # Creamos una marca de tiempo única para que GitHub siempre detecte un cambio
    ahora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    firma = f"\n\n/* 🌙 Retoque nocturno: {ahora} - Diseño seguro sin flashes */\n"

    # Escribimos el archivo: Original + Lo nuevo de la IA + Firma con fecha
    with open(archivo_objetivo, "w") as f:
        f.write(css_actual + "\n" + nuevo_contenido + firma)
    
    print(f"¡Éxito! El archivo {archivo_objetivo} ha sido actualizado.")

except Exception as e:
    print(f"Error durante la ejecución: {e}")
