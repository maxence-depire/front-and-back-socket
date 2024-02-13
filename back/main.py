from flask import Flask

app = Flask()

@app.route("/http/getValue")
def httpget_value():
    return 10

app.run(host="localhost", port=3306, debug=True)