from flask import Flask, request, render_template, redirect, session
from dogs import get_dog, get_dogs,add_dog,delete_dog,get_information,get_breedinfo,get_breeditem

app=Flask(__name__)
app.debug=True
app.secret_key="p"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dogslist")
def dogslist():
    return render_template("dogslist.html", alldogs=get_dogs())

@app.route("/dogpage/<name>")
def dogpage(name):
    return render_template("result.html", dog=get_dog(name))

@app.route("/result")
def result():
    key=request.args["a"]
    keydogs = []
    dogs=get_dogs()
    for dog in dogs:
        if key.lower() in dog['Name'].lower()+dog['Breed'].lower()+dog['Color'].lower():
            keydogs.append(dog)
    if len(keydogs)>0:
        return render_template("dogslist.html", alldogs=keydogs)
    else:
        return "No dogs found <a href='/'>back</a>"

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/modifying")
def modifying():
    if session.get('pass',"")=="AdminPassword":
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
    if len(li)==0:
        return "<body bgcolor='#f5f5dc'></body>You haven't answered any questions"
    else:
        return "<h3>"+li[0].capitalize()+" is the right dog for you!</h3><br>"+get_breedinfo(str(li[0]).title()) + "<body bgcolor='#f5f5dc'></body><br><a href='result?a=" + li[0] + "'</a><br>See which puppies are available<br>" #+get_breedinfo(str(li[0]).title())"
app.run("127.0.0.1",5001)
