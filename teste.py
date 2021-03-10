from bottle_json_pretty import JSONPrettyPlugin
from bottle import Bottle
from scraping import start

app = Bottle(autojson=False)
app.install(JSONPrettyPlugin(indent=2, pretty_production=True))

@app.get('/<name>')
def index(name)
    def index(name):
        resp = start(name)
	return resp
app.run(host='0.0.0.0', port=80)
