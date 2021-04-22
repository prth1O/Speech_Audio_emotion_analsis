from flask import Flask,render_template,request
#import speech_recognition as sr
#from model import chunking,pre
#import pydub
import os
#from model import chunking
#from model import prediction

app= Flask(__name__)



'''
class Speech_emot:
    """docstring fs Speech_emot."""

    def __init__(self):
        self.FolderPath = "InputFiles"
        self.fileList = os.listdir(self.FolderPath)
        self.separatedOutputFiles = "./SeparatedOutputFiles"
        self.outputText = {}

    def process_audio(self):
        for val in self.fileList:
            inputFiles = chunking(os.path.join(self.FolderPath,val), self.separatedOutputFiles)
        pred=prediction(inputFiles)
        outputText['Emot_prediction']=pred
        return inputFiles




    inputFileDir = "./InputFiles"
    archiveDir = './ArchivedInputFiles'
'''
@app.route('/Home')
def index():
    return render_template("index.html")

@app.route('/Result')
def result():
    return render_template('Result.html')
