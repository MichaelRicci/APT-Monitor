from flask import render_template, request, redirect, url_for
from app import scraper, api_integration, db

@app.route('/')
def index():
    # Fetch recent APT activities from the database
    # Display on the homepage
    return render_template('index.html')

@app.route('/results')
def results():
    # Fetch and display scraper results
    return render_template('results.html')

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        # Save user-defined APT keywords or settings
        return redirect(url_for('index'))
    return render_template('settings.html')
