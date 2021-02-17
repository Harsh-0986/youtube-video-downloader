from flask import Flask, render_template, request
# import os
from pytube import YouTube

# TEMPLATE_DIR = os.path.abspath('../templates')
# STATIC_DIR = os.path.abspath('../static')
app = Flask(__name__)

def download_video(link):
    yt = YouTube(link)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/downloading', methods = ['POST', 'GET'])
def get_link():
    if request.method == "GET":
        return "Nothing"
    if request.method =="POST":
        form_data = request.form.getlist('link')
        # for key, value in form_data_list:
        link = str(form_data[0])
        download_video(link)
        return render_template('downloading.html',form_data = form_data)

app.run(debug=True)