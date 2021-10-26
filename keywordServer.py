from flask import Flask
from scraper import get_contents_from_keyword
import analyze 
from flask_cors import CORS
import json
from flask import request


app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/wordcloud')
def wordcloud():
    keyword = request.args.get('keyword')
    sentence = get_contents_from_keyword(keyword)
    # print('result of search',sentence)
    noun_list = analyze.get_nouns_from_sentences(sentence)
    body = {
        "data" : noun_list
    }
    return json.dumps(body, ensure_ascii=False)

if __name__ == '__main__':
    app.run()
