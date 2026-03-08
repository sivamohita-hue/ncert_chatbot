from googletrans import Translator

translator = Translator()

def normalize_query(query):

    # simple Tanglish/Hinglish mapping
    mapping = {
        "enna": "what",
        "epdi": "how",
        "epadi": "how",
        "kyu": "why",
        "kaise": "how",
        "kya": "what",
        "hai": "is",
        "kaun": "who"
    }

    words = query.split()

    normalized = []

    for w in words:
        if w.lower() in mapping:
            normalized.append(mapping[w.lower()])
        else:
            normalized.append(w)

    sentence = " ".join(normalized)

    # translate to English if needed
    translated = translator.translate(sentence, dest="en")

    return translated.text
