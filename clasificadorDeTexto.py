import spacy

# Formato de reglas para imprimir en negrita o formato predeterminado
BOLD = "\033[1m"
RESET = "\033[0m"

# Cargar el modelo en español de spaCy
nlp = spacy.load("es_core_news_sm")

def classify_text(text):
    doc = nlp(text)
    verbs = []
    adjectives = []
    adverbs = []
    pronouns = []
    conjunctions = []

    for token in doc:
        if token.pos_ == "VERB":
            verbs.append(token.text)
        elif token.pos_ == "ADJ":
            adjectives.append(token.text)
        elif token.pos_ == "ADV":
            adverbs.append(token.text)
        elif token.pos_ == "PRON":
            pronouns.append(token.text)
        elif token.dep_ == "cc" or token.dep_ == "mark" or token.dep_ == "case":
            conjunctions.append(token.text)

    return {
        "verbs": verbs,
        "adjectives": adjectives,
        "adverbs": adverbs,
        "pronouns": pronouns,
        "conjunctions": conjunctions
    }

# Leer archivo
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

# Pedir nombre del archivo
filename = input("Nombre del archivo: ")
filename = filename + ".txt"  # nombre del archivo 

# Leer archivo
text = read_file(filename)
if text is None:
    exit()

# Clasificar el texto
resultados = classify_text(text)
print(f"{BOLD}Verbos:{RESET}", resultados["verbs"])
print(f"{BOLD}Adjetivos:{RESET}", resultados["adjectives"])
print(f"{BOLD}Adverbios:{RESET}", resultados["adverbs"])
print(f"{BOLD}Pronombres:{RESET}", resultados["pronouns"])
print(f"{BOLD}Nexos:{RESET}", resultados["conjunctions"])
