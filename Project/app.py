from flask import Flask, render_template, request

app = Flask(__name__)# interface between my server and my application wsgi

import pickle
model = pickle.load(open(r'./rf_tuned.pkl','rb'))

@app.route('/')#binds to an url
def helloworld():
    return render_template("index.html")

@app.route('/login', methods =['POST'])#binds to an url
def login():
    p =request.form["Age"]
    q =request.form["Sex"]
    r =request.form["Bmi"]
    s =request.form["C"]
    t =request.form["Sm"]
    u =request.form["R"]
    
    t=[[int(p),int(q),float(r),int(s),int(t),int(u)]]
    output= model.predict(t)
    print(output)
    
    return render_template("index.html",y = "=" + str(output[0]) )
    


if __name__ == '__main__' :
    app.run(debug= False)