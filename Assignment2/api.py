from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="*")

@app.route('/hello')
def hello():
    return 'Merhaba Dünya!'

if __name__ == '__main__':
    app.run(port=8000, debug=True)
