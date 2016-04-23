from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index_page():
    """Show an index page."""

    return render_template("index.html")

@app.route('/application-form')
def app_form():
    """Shows application form"""

    return render_template("application-form.html")

@app.route('/application', methods=["POST"])
def app_response():
    """Returns response that acknowledges application"""

    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    salary = request.form.get("salary")
    title = request.form.get("title")

    return render_template("applicationresponse.html",
                            firstname=firstname,
                            lastname=lastname,
                            salary=salary,
                            title=title
                            )

if __name__ == "__main__":
    app.run(debug=True)