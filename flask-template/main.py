from flask import flask, render_template, request, redirect, url_for

app = flask (__name__)
@app.route('/')
def home():
    return render_template('index.html', title = "Home Page")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        print("Name: " + {name} + " Email: " + {email}, "Message: " + {message})
        return redirect(url_for("contact"))

    title = "Contact Page"
    return render_template("contact.html", title=title)

if __name__ == '__main__':
    app.run(debug=True)