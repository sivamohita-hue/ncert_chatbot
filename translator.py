from googletrans import Translator

translator = Translator()

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
        translated = translator.translate(sentence, dest="en")
        return translated.text
    except Exception:
        # if translation fails return original sentence
        return sentence
