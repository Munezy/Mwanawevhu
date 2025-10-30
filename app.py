from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for services page
@app.route('/services')
def services():
    return render_template('services.html')

# Route for projects page
@app.route('/projects')
def projects():
    return render_template('projects.html')

# Route for contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# API endpoint for contact form submission
@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')
    # Here you can add logic to save to database or send email
    print(f"Contact form submitted: Name: {name}, Email: {email}, Message: {message}")
    return jsonify({'status': 'success', 'message': 'Thank you for your message!'})

if __name__ == '__main__':
    app.run(debug=True)
