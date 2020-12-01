from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html',
    current_site = 'home')

@app.route('/tjenester')
def services():
    return render_template('services.html',
    current_site = 'services')

@app.route('/nyheter')
def news():
    return render_template('news.html',
    current_site = 'news')

@app.route('/login')
def login():
    return render_template('login.html',
    current_site = 'login')


"""
def get_articles():
    articles = []
    with open('articles.txt') as file:
        for line in file:
            headline, text = line.split(';')
            articles.append((headline,text))
    return articles
@app.route('/articles')
def articles():
    articles = get_articles()
    return render_template('template.html', 
    articles=articles)

    return articles
"""

if __name__ == '__main__':
    app.run()