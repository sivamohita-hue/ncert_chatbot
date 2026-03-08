from deep_translator import GoogleTranslator

def normalize_query(query):

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

    try:
        translated = GoogleTranslator(source="auto", target="en").translate(sentence)
        return translated
    except:
        return sentence
