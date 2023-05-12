from googletrans import Translator

translator = Translator()

def make_translate(word):
    tword_answer = {}
    tword_answer['word'] = word
    try:
        tword = translator.translate(word, dest='uz')
        tword_answer['translate'] = tword.text
    except:
        tword_answer['translate'] = "Bunday so'z topilmadi"
    return tword_answer