from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hi():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run()
