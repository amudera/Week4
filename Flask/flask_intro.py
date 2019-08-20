from flask import Flask, url_for, redirect, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def example_function():
    return "This works"

@app.route('/another_route',methods=['GET'])

def other_route():
    return "<h2> This is a different route </h2>"

@app.route('/login/<username>/<password>',methods=['GET'])

def log_in(username,password):
    if username == 'Greg':
        if password == 'password':
            return redirect('/')
    return redirect(url_for(other_route)

if __name__ == "__main__":
    app.run(debug=True)

