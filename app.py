from flask import Flask, render_template, request, jsonify
from chatbot import process_text


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.form['message']    
    bot_response = process_text(user_message)
    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True)