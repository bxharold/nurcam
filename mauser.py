#!/usr/bin/python3
# mauser.py based on bowser.py  
#  * use venv to  pip install flask-cors
#  * add CORS trash -- denoted below
#  * streaming video is started by python picamera_stream.py
#    here, as subprocess.run([f"python ./picamera_stream.py &"] 
#  * util_functions.py can be run stand-alone on port 5003

from flask import Flask, render_template, request, jsonify, redirect
from util_functions import nucamUTIL_dict, Camstream, getHIP

### ------- ADDED FOR CORS: ----------
from flask_cors import CORS    
app = Flask(__name__)
CORS(app)  

@app.after_request
def handle_options(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, X-Requested-With"
    return response
### ------- END ADDED FOR CORS ------- 

ip, port = getHIP()[0], 5000

@app.route("/cam", methods=["GET"])
def cam(): 
  #####ip, port = "mc24b.local", 8000
  return render_template("nucam.html", ip=ip, port=port)

@app.route("/refresh", methods=["GET"])
def refresh(): 
  ####return render_template("nucam.html", ip=ip, port=port)
  return redirect("/cam")

@app.route("/startstream", methods=["GET"])
def startstream(): 
  camstream.start()
  ####return render_template("nucam.html", ip=ip, port=port)
  return redirect("/cam")

@app.route("/takepicture", methods=["GET"])
def takepicture(): 
  camstream.snapshot()
  ####return render_template("nucam.html", ip=ip, port=port)
  return redirect("/cam")

@app.route("/movie", methods=["GET"])
def movie(): 
  camstream.movie()
  ####return render_template("nucam.html", ip=ip, port=port)
  return redirect("/cam")

@app.route("/killstream", methods=["GET"])
def killstream(): 
  camstream.kill()
  ####return render_template("nucam.html", ip=ip, port=port)
  return redirect("/cam")

@app.route("/pig", methods=["GET"])
def pig(): 
  return render_template("pignew.html")

@app.route("/lizard", methods=["GET"])
def lizard(): 
  return render_template("lizard.html")

@app.route("/answers", methods=["GET"])
def answers(): 
  return render_template("answers.html")

### --   --  --  --  --  --  --  --  --  --  --  --  --  --  -- 
### answer() and heat() were ajax API tests in bowser.html 
### bowser.html is not used in nucam
### answer() and heat() remain as  ajax API tests

@app.route("/", methods=["GET"])       # the API test page
@app.route("/index", methods=["GET"])
def index(): 
  return render_template("mbase.html")

@app.route("/answer", methods=["GET", "POST"])
def answer():
  print("why am I here?")
  data = request.get_json()
  if data is None:
      print(data, "why am I here with None data?")
      #return render_template("main.html")
  print(data, "seriously, why am I here?")
  a =   data.get ( 'a' )
  b = data.get('b')
  c = int(a) * int(b) * -1
  print(a,b,c,"  answer")
  return {'c': c, 'a':a, 'b':b}
  #return jsonify({'c': c, 'a':a, 'b':b})

@app.route("/heat", methods=["GET","POST"])
def heat():
  rv = nucamUTIL_dict()
  return rv
   
if __name__ == '__main__':
    camstream = Camstream()
    port = 5000
    app.run(host="0.0.0.0", port=f"{port}", debug=True)

