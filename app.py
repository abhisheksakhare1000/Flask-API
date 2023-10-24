from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('index.html') 


# API testing
@app.route("/demo", methods=['POST'])
def calculate1 ():
    if request.method == "POST":
        operation = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        result = 0

        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            result = num1 / num2

        return "The result is {}".format(result)
        
        

# getting input through forms

@app.route("/operation", methods=['POST'])
def calculate():
    if request.method == "POST":
        operation = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = 0

        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            result = num1 / num2

        return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
