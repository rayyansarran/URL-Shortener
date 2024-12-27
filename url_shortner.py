from flask import Flask, render_template, request, redirect
import string
import random
import hashlib

app = Flask(__name__)

class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def shorten_url(self, long_url, custom_slug=None):
        if custom_slug:
            short_url = custom_slug
            if short_url in self.url_mapping:
                raise ValueError("Custom slug already in use")
        else:
            short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
            while short_url in self.url_mapping:  # Ensure the generated slug is unique
                short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        self.url_mapping[short_url] = long_url
        return short_url

    def get_original_url(self, short_url):
        return self.url_mapping.get(short_url, "URL not found")

shortener = URLShortener()

@app.route('/', methods=['GET', 'POST'])
def home():
    short_url = None
    error = None
    if request.method == 'POST':
        long_url = request.form['long_url']
        custom_slug = request.form.get('custom_slug')
        try:
            short_url = shortener.shorten_url(long_url, custom_slug)
        except ValueError as e:
            error = str(e)
    return render_template('index.html', short_url=short_url, error=error)

@app.route('/<short_url>')
def redirect_to_original(short_url):
    long_url = shortener.get_original_url(short_url)
    if long_url != "URL not found":
        return redirect(long_url)
    return "URL not found"

if __name__ == "__main__":
    app.run(debug=True)
