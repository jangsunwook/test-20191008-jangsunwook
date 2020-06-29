from flask import Flask, request, render_template , redirect, url_for, abort
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html') 

@app.route('/start')
def start():
    return render_template('start.html')

@app.route('/hello/<name>')
def hellovar(name):
    return 'Hello, {}!' .format(name)

@app.route('/start/<int:num>')
def input_num(num):
    if num ==1:
        return render_template('1.html')
    elif num == 2:
        return render_template('2.html')    
    elif num == 3:
        return render_template('3.html')
    elif num == 4:
        return render_template('4.html')
    elif num == 5:
        return render_template('5.html')
    elif num == 6:
        return render_template('6.html')        
    else:
        return render_template('7.html')        

if __name__ == '__main__':
    
    app.run(debug=True)  