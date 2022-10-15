import json
import os

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/calc', methods = ['POST'])
def calc():
   request.get_json(silent=True, force=True)
   req = req.get("result")
   num1 = int(result.get("parameters").gett("num1"))
   num2 = int(result.get("parameters").gett("num2"))
   speech = ("Sum of {0} and {1} is {2}".format(num1,num2,num1 + num2))

   res = {"speech": speech,
	"displayText": speech
    }
   res = json.dump(res,indent=4)
   r= make_response(res)
   r.headers['Content-Type']= 'application/json'
   return r

if __name__=='__main__':
    port = int(os.getenv('PORT', 5000))
    print("running")
    app.run()