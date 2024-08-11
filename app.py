import flask
from flask import request,render_template
from flask_cors import CORS
import pickle
app=flask.flask(__name__,static_url_path='')

CORS(app)
model=pickle.load(open('iris.plk','rb'))
@app.route('/',methods=['GET'])
def sendhomepage():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])

def predictspecies():
    sl=float(request.form['sl'])
    sw=float(request.form['sw'])
    pl=float(request.form['pl'])
    pw=float(request.form['pw'])
    x=[[sl,sw,pl,pw]]
    species=model.predict(x)[0]
    return render_template('predict.html',predict=species)
if __name__=='__main__':
    app.run(debug=True)
