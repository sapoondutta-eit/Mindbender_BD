from flask import Flask
app = Flask(__name__)

# @app.route('/')
# def hello_world():
# 	return 'hello world'

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name


# @app.route('/')
# def hello_world():
# 	return 'hello world'


# @app.route('/hello/<name>')
# def hello_name(name):
#    return 'Hello %s!' % name


# @app.route('/flask')
# def hello_flask():
#    return 'Hello Flask'

# @app.route('/python/')
# def hello_python():
#    return 'Hello Python'


# @app.route('/admin')
# def hello_admin():
#    return 'Hello Admin'

# @app.route('/guest/<guest>')
# def hello_guest(guest):
#    return 'Hello %s as Guest' % guest

# @app.route('/user/<name>')
# def hello_user(name):
#    if name =='admin':
#       return redirect(url_for('hello_admin'))
#    else:
#       return redirect(url_for('hello_guest',guest = name))



# @app.route('/')
# def index():
#    return render_template("hello.html")

# @app.route('/hello/<user>')
# def hello_name(user):
#    return render_template("hello.html", name = user)

# @app.route('/hello/<int:score>')
# def hello_name(score):
#    return render_template('hello.html', marks = score)



# @app.route('/result')
# def result():
#    dict = {'phy':50,'che':60,'maths':70}
#    return render_template('results.html', result = dict)

if __name__ == '__main__':
   app.run(debug = True)



