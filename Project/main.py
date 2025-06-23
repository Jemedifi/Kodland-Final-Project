from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/calc", methods=["GET", "POST"])
def home():
    display_result = ""
    if request.method == "POST":
        js_variable = request.form.get('jsVariable')
        try:
            if all(char.isdigit() or char in '+-*/.%()' for char in js_variable):
                display_result = str(eval(js_variable))
            else:
                display_result = "Error: Invalid Input"
        except (SyntaxError, TypeError, ZeroDivisionError):
            display_result = "Error"
    return render_template("base.html", display_result=display_result)

if __name__ == "__main__":
    app.run(debug=True)

