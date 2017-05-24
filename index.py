from flask import Flask, request, render_template, redirect, session
from dogs import get_dog, get_dogs,add_dog,delete_dog #импортируем функцию get_dog

app=Flask(__name__) #в переменной app содержится весь сайт
app.debug=True #explains the error
app.secret_key="p"

@app.route("/") #главная страница
def index():
    return render_template("index.html")
#<br> - перенос строки, <a>...</a> - link, <form>

@app.route("/pasha")
def pasha():
    return render_template("pasha.html", alldogs=get_dogs())

@app.route("/dogpage/<name>")
def dogpage(name):
    return render_template("result.html", dog=get_dog(name))

@app.route("/result")
def result():
    key=request.args["a"]
    keydogs = []
    dogs=get_dogs()
    for dog in dogs:
        if key in dog['Name'].lower()+dog['Breed'].lower()+dog['Color'].lower():
            keydogs.append(dog)
    if len(keydogs)>0:
        return render_template("pasha.html", alldogs=keydogs)
    else:
        return "No dogs found <a href='/'>back</a>"

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/modifying")
def modifying():
    if session.get('pass',"")=="pash":
        return render_template("modifying.html",alldogs=get_dogs(),text=request.args.get("text",""))
    else:
        return redirect("/login")

@app.route("/log_out")
def log_out():
    session['pass']=""
    return redirect("/")

@app.route("/addDog")
def addDog():
    add_dog(request.args)
    return redirect("/modifying?text=Success!")

@app.route("/deleteDog/<name>")
def deleteDog(name):
    delete_dog(name)
    return redirect("/modifying")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/logging")
def logging():
    session['pass']=request.args['pass']
    return redirect("/modifying")

@app.route("/testing")
def testing():
    dic = request.args
    rates = {}
    for n in dic:
        breeds = dic[n].split(",")
        for breed in breeds:
            rates[breed.lower().strip()] = rates.get(breed.lower().strip(), 0) + 1
    li = list(rates.items())
    li.sort(key = lambda x: 0-x[1])
    li = [n[0] for n in li]
    # в li лежат породы в порядке убывания 
    return li[0].capitalize() +" is the right dog for you!<br><a href='result?a=" + li[0] + "'</a>See which puppies are available"
        
    

#"Порода "+ get_dog(text)['breed']

#app.run()
app.run("127.0.0.1",5001)
