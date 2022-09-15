# imported all esential libraries
from email.mime import application
from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

web_app = Flask(__name__)

# loading the previously created model
model=pickle.load(open('final_model.pkl','rb'))


@web_app.route('/')
def hello_world():
    return render_template("website.html")


@web_app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict_proba(final)
    output='{0:.{1}f}'.format(prediction[0][1], 2)

    if output>str(0.5):
        return render_template('forest_fire.html',pred='the model says you are male.\nProbability of being male is {}'.format(output),bhai="kuch karna hain iska ab?")
    else:
        return render_template('forest_fire.html',pred='the model says you are male..\n Probability of being female is {}'.format(output),bhai="Your Forest is Safe for now")


if __name__ == '__main__':
    web_app.run(debug=True)