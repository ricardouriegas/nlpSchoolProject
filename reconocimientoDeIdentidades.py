import spacy
from deep_translator import GoogleTranslator

# Formateo de texto para negritas o formato predeterminado al imprimir
BOLD = "\033[1m"
RESET = "\033[0m"

# Cargar el modelo en inglés de spaCy
nlp = spacy.load('en_core_web_sm')

def   recognize_entities(text):
    doc = nlp(text)

    # Diccionario para mapear las etiquetas a sus descripciones en lenguaje natural
    etiquetas_descripciones = {
        "PERSON": "Nombre propio",
        "NORP": "Grupo étnico o nacionalidad",
        "FAC": "Edificio o lugar",
        "ORG": "Organización",
        "GPE": "Lugar",
        "LOC": "Lugar",
        "PRODUCT": "Producto",
        "EVENT": "Evento",
        "WORK_OF_ART": "Obra de arte",
        "LAW": "Ley",
        "LANGUAGE": "Idioma",
        "DATE": "Fecha",
        "TIME": "Hora",
        "PERCENT": "Porcentaje",
        "MONEY": "Moneda",
        "QUANTITY": "Cantidad",
        "ORDINAL": "Ordinal",
        "CARDINAL": "Cardinal"
    }

    # Diccionario para almacenar las entidades agrupadas por etiqueta
    entidades_por_etiqueta = {}

    # Definir el traductor
    translator = GoogleTranslator(source='en', target='es')

    # Obtener entidades etiquetadas y traducirlas
    for entidad in doc.ents:
        entidad_ingles = entidad.text
        etiqueta = entidad.label_
        descripcion = etiquetas_descripciones.get(etiqueta, etiqueta)

        if descripcion not in entidades_por_etiqueta:
            entidades_por_etiqueta[descripcion] = []

        # Traducir entidad a inglés usando deep_translator
        entidad_espanol = translator.translate(entidad_ingles, source='en', target='es')
        entidades_por_etiqueta[descripcion].append(entidad_espanol)

    return entidades_por_etiqueta

# Ejemplo de texto
def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"El archivo '{filename}' no existe.")
        return None

#######################################
#                MAIN                 #
#######################################

# Pedir el nombre de archivo del texto
filename = input("Nombre del archivo: ")
filename = filename + ".txt"  # nombre del archivo 

text = read_file(filename)
if text is None:
    exit()

# Reconocer entidades en el texto
entidades_reconocidas = recognize_entities(text)

# Imprimir con formato
for descripcion, entidades in entidades_reconocidas.items():
    print(f"{BOLD}{descripcion}: {RESET}{entidades}")