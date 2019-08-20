from flask import Flask, request, render_template, redirect, session

app = Flask(__name__)
app.secret_key = "The session needs this"

@app.route('/',methods=['GET'])
def send_to_login():
    if 'username' in session:
        return redirect ('/homepage')
    else:
        return redirect('/login')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else: 
        username = request.form['username']
        password = request.form['password']
        print(username,password)
        if check_user(username,password):
            session['username'] = username
            return redirect ('/homepage')
        else:
            return render_template('/login.html',message='login failed') #render template doesnt reload or refresh the page
            #render template just changes the way your page looks but wouldnt log you out
    
    @app.route('/logout',methods=['GET'])
    def log_out():
        session.pop('username',None)
        return redirect('/login')
    
    def check_user(username,password):
        if username == 'GREG' and password == 'Password':
            return True
        return False

    if __name__=='__main__':
        app.run(debug=True)
    


