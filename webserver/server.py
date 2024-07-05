import csv

from flask import Flask, render_template, request, redirect

app = Flask(__name__, static_folder='static', static_url_path='/')


@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/about.html")
def about_page():
    return render_template("about.html")

@app.route("/loc.html")
def loc_page():
    return render_template("loc.html")

@app.route("/contact.html")
def contact_page():
    return render_template("contact.html")

@app.route("/onebedroom.html")
def onebedroom_page():
    return render_template("onebedroom.html")

@app.route("/twobedroom.html")
def twobedroom_page():
    return render_template("twobedroom.html")

@app.route("/studio.html")
def studio_page():
    return render_template("studio.html")

@app.route("/studiop.html")
def stuiop_page():
    return render_template("studiop.html")

@app.route("/rooms.html")
def rooms_page():
    return render_template("rooms.html")


# @app.route("/<string:page_name>")
# def html_page(page_name):
#     return render_template(page_name)


# def write_to_csv(data):
#     with open('database.csv', newline='', mode='a') as database:
#         name = data["name"]
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#         csv_writer.writerow([name, email, subject, message])
#
#
# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     if request.method == 'POST':
#         try:
#             data = request.form.to_dict()
#             write_to_csv(data)
#             return redirect('/thanku.html')
#         except:
#             return 'Did not save to database'
#     else:
#         return 'Something went wrong. Please try again.'
