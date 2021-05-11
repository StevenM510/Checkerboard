from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/<int:number>')
@app.route('/<int:number>/<string:color>')
def checkerboard(number = 8, color = 'color'):
    return render_template('index.html', color = color, number = number )

if __name__=="__main__":
    app.run(debug=True)