from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    title = "Expert Design"
    return render_template('index.html', data = title)

@app.route('/contact')
def contact():
    return "contact"

if __name__ == '__main__':
    app.run(debug=True)
