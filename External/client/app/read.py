import os
import requests as req

#os.environ['NO_PROXY'] = '0.0.0.0'
#x = req.get("https://0.0.0.0:5000/")
x = req.get("http://10.0.0.246:5000/")
print(x.text)