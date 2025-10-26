from flask import Flask,request,redirect,url_for,session,Response

# Create a Flask app instance
app = Flask(__name__)
app.secret_key='supersecret'

#Login Page
@app.route('/',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']

        if username and password:
            session['user']=username
            return redirect(url_for('welcome'))
        else:
            return Response('Invalid credentials.please try again.',mimetype='text/plain')
        
    return '''
        <h2>Login Page</h2>
        <form method="post">
            Username:<input type="text" name="username"<br>
            Password:<input type="text" name="password"<br>
            <input type="submit" value="Login">
            <form>
            '''

@app.route("/welcome")
def welcome():
    if 'user' in session:
        return f'''
        <h2>Welcome,{session['user']}!</h2>
        <a href={url_for('logout')}>Logout</a>
'''
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
