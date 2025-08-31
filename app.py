from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
stack = []  # Global stack list

@app.route('/')
def index():
    return render_template('index.html', stack=stack)

@app.route('/push', methods=['POST'])
def push():
    value = request.form.get('value')
    if value:
        stack.append(value)
    return redirect(url_for('index'))

@app.route('/pop', methods=['POST'])
def pop():
    if stack:
        stack.pop()
    return redirect(url_for('index'))

@app.route('/clear', methods=['POST'])
def clear():
    stack.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
