from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index_page():
    """Show an index page."""

    return render_template("index.html")

@app.route('/applicationform')
def app_form():
    """Shows application form"""

    return render_template("applicationform.html")

@app.route('/application')
def app_response():
    """Returns response that acknowledges application"""

    first_name = request.args.get("firstname")
    last_name = request.args.get("lastname")
    salary = request.args.get("salary")
    title = request.args.get("jobtitle")

    return render_template("applicationresponse.html",
                            firstname=first_name,
                            lastname=last_name,
                            salary=salary,
                            title=title
                            )

if __name__ == "__main__":
    app.run(debug=True)