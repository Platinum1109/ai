from flask.templating import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    a = ":D"
    return """
    <html>
        <head>
            <title> Home - Simple Flask App</title>
        </head>
        <body>
            <div><a href="/test">Test Page</a><div>
            <div><a href="/test2">Test2 Page</a><div>"""+ a +'''     </body>
    </html>
    '''
@app.route('/about')
def about():
    return "About"

@app.route('/test')
def test():
    user = {'username':" Anson"}
    return render_template('test.html', user=user)

@app.route('/test2')
def test2():
    user={'username':' Anson'}
    sample_data=[
        {
            'author':{'username':'Anson'},
            'body':'Hello!',
            'year': '2021'
        },{
            'author': {'username':'Anson'},
            'body':'Welcome to Flask!'
        }
    ]
    return render_template('test2.html', user=user, sample_data=sample_data)