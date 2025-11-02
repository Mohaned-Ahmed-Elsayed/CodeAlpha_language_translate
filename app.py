from flask import Flask, render_template, request
from deep_translator import GoogleTranslator
import webbrowser
from threading import Timer

app = Flask(__name__)

# Supported languages (simplified list)
LANGUAGES = {
    'en': 'English',
    'ar': 'Arabic',
    'fr': 'French',
    'es': 'Spanish',
    'de': 'German',
    'it': 'Italian',
    'zh-CN': 'Chinese (Simplified)',
    'ja': 'Japanese',
    'ru': 'Russian'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ''
    source_lang = ''
    target_lang = ''
    input_text = ''

    if request.method == 'POST':
        input_text = request.form['text']
        source_lang = request.form['source_lang']
        target_lang = request.form['target_lang']

        if input_text:
            translated_text = GoogleTranslator(source=source_lang, target=target_lang).translate(input_text)

    return render_template('index.html',
                           languages=LANGUAGES,
                           translated_text=translated_text,
                           input_text=input_text,
                           source_lang=source_lang,
                           target_lang=target_lang)

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(debug=True,use_reloader=False)

