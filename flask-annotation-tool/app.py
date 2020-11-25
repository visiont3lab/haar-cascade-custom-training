from flask import Flask,url_for, request
from flask import render_template
import os 

filename = "res.txt"
if not os.path.exists(filename):
    f=open(filename,"w")
    f.close()

# useful info: https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application
app = Flask(__name__, static_folder='static')

static_path = os.path.join(".", "static")
folder_path =  "images/"
full_static_path = os.path.join(static_path, folder_path)
names = os.listdir(full_static_path)
i = 0

@app.route('/')
def index():
    path = os.path.join(folder_path,names[i])
    image_file = url_for('static', filename=path)
    return render_template('index.html', filename=names[i], value=i, total=len(names), image_file=image_file)

@app.route('/previous')
def prevfunc():
    path = None
    global i
    if i> 0:
        i = i -1
        path = os.path.join(folder_path,names[i])
    else:
        path = os.path.join(folder_path,names[i])

    image_file = url_for('static', filename=path)
    return render_template('index.html', filename=names[i], value=i, total=len(names), image_file=image_file)

@app.route('/next')
def nextfunc():
    path = None
    global i
    if i>= 0 and i< len(names):
        i=i+1
        path = os.path.join(folder_path,names[i])
    else:
        path = os.path.join(folder_path,names[i])    
    image_file = url_for('static', filename=path)
    return render_template('index.html', filename=names[i], value=i, total=len(names), image_file=image_file)

@app.route('/save', methods=['GET','POST'])
def savefunc():
    resposne = None
    if request.method == "POST":   
        x = request.json["x"];
        y = request.json["y"];
        w = request.json["width"];
        h = request.json["height"];
        print(x,y,w,h)
        f=open(filename,"a+")
        f.write(os.path.join(full_static_path,names[i]) + " " + str(1) + " " + str(x) + " " + str(y) + " " + 
            str(w) + " " + str(h) + "\n")
        f.close()
        

        
        response =  { 'Status' : 'Success'}
    return response


@app.route('/start', methods=['POST'])
def startfunc():
    ivalue = int(request.form['start'])
    #print(value)
    path = None
    global i
    i = ivalue
    if i>= 0 and i< len(names):
        i=i+1
        path = os.path.join(folder_path,names[i])
    else:
        path = os.path.join(folder_path,names[i])    
    print(path)
    image_file = url_for('static', filename=path)
    return render_template('index.html', filename=names[i], value=i, total=len(names), image_file=image_file)


app.run(debug = True)