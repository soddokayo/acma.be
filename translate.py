from googletrans import Translator

tr = Translator()

def translate(req):
    translated = tr.translate(req)
    res = translated.text
    return res