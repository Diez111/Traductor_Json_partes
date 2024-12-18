import json
import time
from deep_translator import GoogleTranslator
from concurrent.futures import ThreadPoolExecutor, as_completed

def translate_chunk(chunk, target_language="es"):
    """
    Traduce un bloque de frases.
    """
    translator = GoogleTranslator(source='auto', target=target_language)
    translated_chunk = []
    for item in chunk:
        try:
            translated_text = translator.translate(item["text"])
            translated_chunk.append({"text": translated_text, "author": item["author"]})
        except Exception as e:
            print(f"Error al traducir: {e}")
            translated_chunk.append({"text": item["text"], "author": item["author"]})
            time.sleep(1)  # Pausa corta para evitar bloqueos
    return translated_chunk

def translate_json_parallel(input_path, output_path, target_language="es", chunk_size=50, max_workers=4):
    """
    Traduce un archivo JSON en paralelo, guarda progreso incremental y permite seguimiento.
    """
    # Cargar datos de entrada
    with open(input_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    total_quotes = len(data["quotes"])
    print(f"Total de frases a traducir: {total_quotes}")

    # Dividir las frases en bloques
    chunks = [data["quotes"][i:i + chunk_size] for i in range(0, total_quotes, chunk_size)]
    translated_quotes = {"quotes": []}

    # Proceso de traducción en paralelo
    with ThreadPoolExecutor(max_workers=max_workers) as executor, open(output_path, 'w', encoding='utf-8') as out_file:
        futures = {executor.submit(translate_chunk, chunk, target_language): i for i, chunk in enumerate(chunks)}

        # Procesar resultados a medida que terminan
        for future in as_completed(futures):
            chunk_index = futures[future]
            print(f"Bloque {chunk_index + 1}/{len(chunks)} traducido.")

            # Guardar resultados parciales
            try:
                translated_chunk = future.result()
                translated_quotes["quotes"].extend(translated_chunk)
                # Guardar progreso incremental
                out_file.seek(0)
                json.dump(translated_quotes, out_file, ensure_ascii=False, indent=4)
                out_file.truncate()
            except Exception as e:
                print(f"Error en el bloque {chunk_index + 1}: {e}")

    print(f"Traducción completada. Archivo guardado en: {output_path}")

# Rutas de archivo
input_file = "/home/diez/Descargas/quotes.json"
output_file = "/home/diez/Descargas/quotes_translated.json"

# Ejecutar la función
translate_json_parallel(input_file, output_file)
