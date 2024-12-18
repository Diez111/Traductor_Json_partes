# **Traductor_Json_partes**

Este script traduce frases almacenadas en un archivo JSON a un idioma objetivo usando la librería **deep_translator**. Está diseñado para ejecutarse en **Ubuntu** y utiliza procesamiento paralelo para mejorar el rendimiento.

---

## **Requisitos previos**

### 1. **Instalar Python y pip**  
Abre una terminal y ejecuta:

```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

### 2. **Instalar las dependencias necesarias**  
Instala la librería `deep_translator`:

```bash
pip3 install deep_translator
```

---

## **Configuración**

1. **Descarga el script**  
   Clona el repositorio desde GitHub:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <nombre-del-repositorio>
   ```

2. **Prepara el archivo JSON**  
   Coloca tu archivo `quotes.json` con la estructura adecuada:

   ```json
   {
       "quotes": [
           {"text": "Frase original", "author": "Autor"}
       ]
   }
   ```

---

## **Ejecución del script**

Ejecuta el script desde la terminal con Python 3:

```bash
python3 translate_quotes.py
```

El script buscará los archivos en las siguientes rutas predeterminadas:
- Entrada: `/home/diez/Descargas/quotes.json`
- Salida: `/home/diez/Descargas/quotes_translated.json`

---

## **Personalización**

- **Idioma de destino:** Cambia `target_language` en el script (por defecto, `"es"` para español).  
- **Tamaño de bloque:** Modifica `chunk_size` para procesar más o menos frases por bloque.  
- **Archivo de entrada/salida:** Edita las variables `input_file` y `output_file` en el script.

---

## **Ejemplo de resultado**

**Entrada:**
```json
{"text": "The obstacle is the way.", "author": "Marcus Aurelius"}
```

**Salida:**
```json
{"text": "El obstáculo es el camino.", "author": "Marcus Aurelius"}
```

---

## **Notas adicionales**
- Asegúrate de tener conexión a Internet.  
- Guarda progreso incremental para evitar pérdida de datos.  
- Usa el script en archivos grandes sin problemas gracias a la ejecución en paralelo.

---

¡Listo! Puedes traducir tus frases a cualquier idioma de forma rápida y eficiente. 🚀
