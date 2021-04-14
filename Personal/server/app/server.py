from flask import Flask, request, jsonify
server = Flask(__name__)

@server.route("/",  methods=['GET', 'POST'])
def hello():
    file1 = open("info.txt","r")
    list = []
    i = 0
    for x in file1:
        list.append(x)
    return jsonify(list)

if __name__ == "__main__":
   server.run(host='0.0.0.0')