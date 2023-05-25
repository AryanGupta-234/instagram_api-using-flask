from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import insta_api
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import os

scheduler = BackgroundScheduler()
app = Flask(__name__,template_folder='templates', static_folder='static')
try:
    os.makedirs(os.path.join(os.path.expanduser('~'), 'Windows', "uploads"))
except:
    pass    
# os.path.join(os.path.expanduser('~'), 'Windows', "uploads")
app.config['UPLOAD_FOLDER']=os.path.join(os.path.expanduser('~'), 'Windows', "uploads")
# app.config['UPLOAD_FOLDER'] = '/home/aaryangupta/mysite/uploads/'

jobs = []
user_name=""
pass_word=""
# Schedule the tasks dynamically




@app.route('/')
def index():
    return render_template('login_page.html')



@app.route('/login_form', methods=['POST'])
def login_form():
    if request.method == 'POST':
        user = request.form['username']
        passwd = request.form['password']
        stat=insta_api.login(user,passwd)
        if stat==True:
            user_name=user
            pass_word=passwd
            return render_template('insta frontend.html',username=user_name)        
        else:
            user_name=""
            pass_word=""
            return 


# def index():
#     return render_template('insta frontend.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    if request.method == 'POST':
        file = request.files['media-path']
        caption = request.form['caption']
        shedule =request.form['schedule']
        tags =request.form['tags']
        print(shedule)
        print(file)
        date=(shedule.split("-"))
        time=(shedule.split("-")[2]).split("T")
        timeh=time[1].split(":")
        print(time,date)
        y=date[0]
        m=date[1]
        d=time[0]
        h=timeh[0]
        mt=timeh[1]
        print(y,m,d,h,mt)
        
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) 
            insta_api.upload_reel(os.path.join(app.config['UPLOAD_FOLDER'], filename),caption,tags)
            # jobs.append(scheduler.add_job(lambda:insta_api.upload_reel(os.path.join(app.config['UPLOAD_FOLDER'], filename),caption), 'date', run_date=datetime(int(y), int(m), int(d), int(h), int(mt))))
            # scheduler.start()
            
    return render_template('insta frontend.html')        

if __name__ == "__main__":
    # app.config['UPLOAD_FOLDER'] = 'path/to/uploads/directory'    
    app.run(debug=True,host='0.0.0.0')

