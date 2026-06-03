from flask import Flask, request, jsonify, render_template
from fsm import Rekrutmen

app = Flask(__name__)
bot = Rekrutmen()

@app.route('/')
def home():
    return render_template('lowongan.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    bot.proses(data['message'])
    return jsonify({"response": bot.respon})

if __name__ == '__main__':
    app.run(debug=True)