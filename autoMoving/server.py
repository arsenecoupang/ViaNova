from flask import Flask, request

app = Flask(__name__)
latest_message = ""

@app.route('/update', methods=['POST'])
def update_message():
    global latest_message
    latest_message = request.form['message']
    return "Message received", 200

@app.route('/message', methods=['GET'])
def get_message():
    return latest_message, 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == '__main__':
    app.run(debug=True)