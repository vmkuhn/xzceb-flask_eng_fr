from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = translator.english_to_french(textToTranslate) # Write your code here
    return translated_text #"Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = translator.french_to_english(textToTranslate) # Write your code here
    return translated_text #"Translated text to English"

@app.route("/")
def renderIndexPage():
    return render_template('index.html') # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
