from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def  Index():
    return render_template('index.html')

@app.route('/tabacos')
def  Tabacos():
    return render_template('tabacos.html')


if __name__ == '__main__':
    app.run()
