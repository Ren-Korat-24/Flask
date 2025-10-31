from flask import Flask,request,redirect,flash,url_for,session,Response,render_template

# Create a Flask app instance
app = Flask(__name__)
app.secret_key='supersecret'

#Home Page
@app.route('/',methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form.get('name')
        if not name:
            flash('Name is required!')
            return redirect(url_for("form"))  
        flash(f'Thanks {name},your feedback was saved!')
        return redirect(url_for("thankyou"))  
    return render_template('form.html')

#Form page
@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)

