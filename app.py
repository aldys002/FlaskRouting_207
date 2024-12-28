from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return f"<h1>Welcome, {name}!</h1>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('nm')
        return redirect(url_for('success', name=user))
    return render_template('login.html')  # Menggunakan file HTML dari templates

if __name__ == '__main__':
    app.run(debug=True)
