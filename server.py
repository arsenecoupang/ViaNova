from flask import Flask, request, jsonify

app = Flask(__name__)
messages = []

@app.route('/update', methods=['POST'])
def update_message():
    global messages
    messages.append(request.form['message'])
    return "Message received", 200

@app.route('/message', methods=['GET'])
def get_message():
    response = jsonify(messages=messages)
    response.headers.add('Content-Type', 'application/json; charset=utf-8')
    return response

if __name__ == '__main__':
    app.run(debug=True)