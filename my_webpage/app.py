from flask import Flask, render_template, url_for, request, redirect
import os, datetime
import modules
#app definition
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html', results="results")

@app.route('/indexde/', methods=['POST','GET'])
def indexde():
    return render_template('indexde.html', results="results")

@app.route('/indexen/', methods=['POST','GET'])
def indexen():
    return render_template('indexen.html', results="results")


@app.route('/myprojects/', methods=['POST','GET'])
def myprojects():
    return render_template('myprojects.html', results="results")

@app.route('/myprojectsen/', methods=['POST','GET'])
def myprojectsen():
    return render_template('myprojectsen.html', results="results")

@app.route('/myprojectsde/', methods=['POST','GET'])
def myprojectsde():
    return render_template('myprojectsde.html', results="results")


@app.route('/certs/', methods=['POST','GET'])
def certs():
    return render_template('certs.html', results="results")

@app.route('/certsen/', methods=['POST','GET'])
def certsen():
    return render_template('certsen.html', results="results")

@app.route('/certsde/', methods=['POST','GET'])
def certsde():
    return render_template('certsde.html', results="results")

@app.route('/contact/', methods=['POST','GET'])
def contact():

    if request.method == 'POST':
        email = request.form.get('email')
        message = request.form.get('message')
        
        #send email to logfile:
        f = open("./log_message.txt",'a')
        date_time = datetime.datetime.now()
        f.write('DATE:'+str(date_time)+'\tLanguage:PL'+'\tEmail:'+str(email)+'\tMessage:'+str(message)+'\n')
        f.close()

        try:
            modules.add_message_to_db("PL", email, message)
            modules.log_to_db("my_webpage","insert_message_to_db_pl", "correct")
        except Exception as e:
            modules.log_to_db("my_webpage","insert_message_to_db_pl", "Error"+str(e))

        return render_template("contact.html", result="results")
    else:
        return render_template('contact.html', results="results")

@app.route('/contacten/', methods=['POST','GET'])
def contacten():
    if request.method == 'POST':
        email = request.form.get('email')
        message = request.form.get('message')
        
        #send email to logfile:
        f = open("./log_message.txt",'a')
        date_time = datetime.datetime.now()
        f.write('DATE:'+str(date_time)+'\tLanguage:EN'+'\tEmail:'+str(email)+'\tMessage:'+str(message)+'\n')
        f.close()
        try:
            modules.add_message_to_db("EN", email, message)
            modules.log_to_db("my_webpage","insert_message_to_db_en", "correct")
        except Exception as e:
            modules.log_to_db("my_webpage","insert_message_to_db_en", "Error"+str(e))
        return render_template("contacten.html", result="results")
    else:
        return render_template('contacten.html', results="results")


@app.route('/contactde/', methods=['POST','GET'])
def contactde():
    if request.method == 'POST':
        email = request.form.get('email')
        message = request.form.get('message')
        
        #send email to logfile:
        f = open("./log_message.txt",'a')
        date_time = datetime.datetime.now()
        f.write('DATE:'+str(date_time)+'\tLanguage:DE'+'\tEmail:'+str(email)+'\tMessage:'+str(message)+'\n')
        f.close()
        try:
            modules.add_message_to_db("DE", email, message)
            modules.log_to_db("my_webpage","insert_message_to_db_de", "correct")
        except Exception as e:
            modules.log_to_db("my_webpage","insert_message_to_db_de", "Error"+str(e))
        return render_template("contactde.html", result="results")
    else:
        return render_template('contactde.html', results="results")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080,debug=True)
