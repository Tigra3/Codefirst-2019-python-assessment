from flask import Flask, render_template
from Youtube_data_app import nJB, nLC


app = Flask("MyApp")

@app.route("/")
def project():
    return render_template("Project_page1.html")


@app.route("/page2")
def project2(nJB, nLC):
   return render_template("Project_page2.html", nJB, nLC)

app.run(debug=True)
