from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        if name and email:            
            response = make_response(redirect(url_for('greeting')))
            response.set_cookie('u_name', name)
            response.set_cookie('u_email', email)
            return response
        else:
            return render_template('form.html')
    return render_template('form.html')

@app.route('/greeting/', methods=['GET', 'POST'])
def greeting():
    if request.method == 'POST':
        response = make_response(redirect(url_for('form')))
        # response = make_response(render_template('/'))
        response.delete_cookie('u_name')
        response.delete_cookie('u_email')
        return response
    return render_template('greeting.html', name=request.cookies.get('u_name'))

if __name__ == '__main__':
    app.run(debug=True)