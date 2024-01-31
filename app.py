from flask import Flask, render_template, request

#Creating an instance 
app=Flask(__name__)

@app.route('/')
def home(): 
   return render_template('home.html') # Render your home page template
    
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/user/<username>')
def greet_user(username):
    return render_template('user.html', username=username)

     

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        
        name = request.form['name']  # Access submitted name
        email = request.form['email']  # Access submitted email
        
        return render_template('thankyou.html', name=name, email=email)  # Display thank you message
    return render_template('submit.html')  # Show the form on GET

    
@app.route('/thank_you')
def thank_you():
    return render_template('submit.html')  # Render the thank you template

    