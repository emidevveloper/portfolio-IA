import google.generativeai as genai
import os

# Configuración de Gemini usando el Secret de GitHub
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

archivo_objetivo = "style.css"

# 1. Leer el código actual (si no existe, crea una base)
if os.path.exists(archivo_objetivo):
    with open(archivo_objetivo, "r") as f:
        css_actual = f.read()
else:
    css_actual = "/* Estilo base */"

# 2. El Prompt: Le damos personalidad a la IA
prompt = f"""
Actúa como un diseñador web creativo y algo rebelde. 
Tu tarea es modificar este archivo CSS para que la web tenga un toque 'cyberpunk' o 'nocturno'.
Añade estilos neón, sombras brillantes o fuentes modernas. 
IMPORTANTE: Mantén lo que ya existe y añade tus cambios al final con comentarios.
CÓDIGO ACTUAL:
{css_actual}
"""

# 3. Generar la "locura"
try:
    response = model.generate_content(prompt)
    nuevo_css = response.text
    
    # Limpiamos posibles etiquetas de Markdown que a veces pone la IA
    nuevo_css = nuevo_css.replace("```css", "").replace("```", "")

    # 4. Guardar cambios
    with open(archivo_objetivo, "w") as f:
        f.write(nuevo_css)
    print("CSS actualizado con éxito por Gemini.")
except Exception as e:
    print(f"Error al contactar con la IA: {e}")