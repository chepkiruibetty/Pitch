from flask import Flask, render_template, url_for,flash,redirect
# from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY']='0727325535'

posts=[
    {
    'author':'Bettyb',
    'title':'Blog Post 1',
    'content':'First Post content',  
    'date_posted': 'Feb 1,2020' 
    },
    {
    'author':'Gakii seron',
    'title':'Blog Post 2',
    'content':'First Post content',  
    'date_posted': 'Feb 3,2020' 
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')
