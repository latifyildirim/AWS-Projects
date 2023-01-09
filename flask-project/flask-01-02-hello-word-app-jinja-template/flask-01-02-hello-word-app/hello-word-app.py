from flask import Flask 

app = Flask(__name__)

@app.route('/')
def head():
    return 'Naber la Latiff'

@app.route('/second')
def second():
    return 'This is second page'

@app.route('/third')
def third():
    return 'This is third page'

@app.route('/forth/<string:id>')
def forth(id,a):
    return f'Id of this page is {id,a}'

if __name__ == '__main__':
    app.run(debug=True)