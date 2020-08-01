#Dependencies
from flask import Flask, render_template, request, jsonify
import simplejson as json

# Constants
TIME_LIM = 60

# Flask Init
app = Flask(__name__)

#Timer & Countdown
def countdownGen(t):
	return (t-i for i in range(t))

gen = countdownGen(TIME_LIM)

@app.route('/_timer', methods=['GET'])
def timer():
	try:
		return jsonify(result=json.dumps(next(gen)))
	except StopIteration:
		return jsonify(result=0)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        return render_template('index.html')
    else:
        return render_template('index.html')

# Flask RUN:
if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=False)
