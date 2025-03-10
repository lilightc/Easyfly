from googletrans import Translator
translate = Translator()
result = translate.translate('北京首都机场')
print(result.text)