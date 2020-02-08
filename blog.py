from datetime import datetime
import Flask, render_template, url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY']='0727325535'
app.config['SQLALCHEMY_DATABASE_URL']='sqlite:///site.db'
db=SQLAlchemy(app)

class User(db.model):
    id=db.Column(db.integer,primary_key=True)
    username=db.Column(db.String(120),unique=True,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
    password=db.Column(db.String(60),nullable=False)
    posts=db.relationship('Post',backref='author,'lazy=True)
    
    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.username}')"
    
    
class Post(db.model):
    id=db.Column(db.Interger,primary_key=True)
    title==db.Column(db.String(100),nullable=False
    date_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow())
    content=db.Column(db.Text,nullable=False)
    user_id=db.Column(db.Inte ger,db.ForeignKey('user.id'),nullable=False)
    
    def __repr__(self):
        return f"User('{self.title}','{self.email}','{self.date_posted}')"
        
    
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

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
