from flask import Flask,render_template,request
import math
app = Flask(__name__)


import datetime
@app.route('/')
def home():
    return render_template('cinque_5.html')

@app.route('/FigureGeo', methods = ['POST'])
def figure():
    figure = request.form["figure"]

    return render_template('cinque_5.html')
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
