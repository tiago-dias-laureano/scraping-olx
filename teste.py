from bottle import route, run, template
from scraping import start 

@route('/<name>')
def index(name):
	resp = start(name)
    return template('{{resp}}', resp=resp)

run(host='localhost', port=8080)