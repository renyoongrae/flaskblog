from flask import Flask, render_template, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '969ee24a8f87a95d65b05677b6e5a765'

posts = [
    {
        'author': 'Ren Nam',
        'title': 'Blog Post 1',
        'content': 'first post content',
        'date_posted': 'Jan 1st, 2019'
    },
    {
        'author': 'Ren Nam',
        'title': 'Blog Post 2',
        'content': '2nd post content',
        'date_posted': 'Jan 8th, 2019'
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

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
