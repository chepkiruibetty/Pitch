from flask import Flask, render_template, url_for,flash,redirect
# from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY']='0727325535'

posts=[
    {
    'title':'RIP President Moi',
    'content':'The country will remember you for the great leadership',  
    'date_posted': 'Feb ,7,2020' 
    },
    {
    'title':'Dev.to',
    'content':'What I Learned about SEO from using JS frameworks',  
    'date_posted': 'Feb 6,2020' 
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')
