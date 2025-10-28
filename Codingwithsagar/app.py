from flask import Flask,request,redirect,url_for,session,Response,render_template

# Create a Flask app instance
app = Flask(__name__)
app.secret_key='supersecret'

#Home Page
@app.route('/')
def home():
    return render_template('home.html')

#Form page
@app.route('/about')
def about():
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)

