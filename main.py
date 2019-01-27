import os
from googletrans import Translator
import os
import time
import sys
import RPi.GPIO as GPIO
from time import sleep



GPIO.setmode(GPIO.BCM)
servo_pin = 2
sleeptime=1

def translate(content):
    translator = Translator()
    content = translator.translate(content).text
    return content
    

def reading(page_number):
    stri = 'cd Desktop'
    os.system(stri)
    
    page = str(page_number)
    stri = 'fswebcam -r 1280x720 --no-banner book/page' + page + '.jpg'
    #fswebcam -r 1280x720 --no-banner book/page.jpg
    os.system(stri)

    stri = 'tesseract book/page' + page + '.jpg booktext/page' + page + ' -l eng+jpn'
    os.system(stri)
    
    textfile = 'booktext/page' + page +'.txt'
    
    with open(textfile , 'r') as content_file:
        content = content_file.read()
    
    print('processing done')
    return content


def speaking(content):
    stri = "espeak -ven+f3 '" + content + "'"
    os.system(stri)

#while True:
#    input_state = GPIO.input(switch_pin) #Read and store value of input to a variable
#    print (input_state)
    
#    if input_state == False:

def convert_to_pdf(page_number):

    stri = 'convert'
    
    for i in range (0, page_number):
        stri = stri + ' book/page' + str(i) + '.jpg'
    
    stri = stri + ' book.pdf'
    return stri

page_number = 2

for i in range (0, page_number):
    string = reading(i)
    string = translate(string)
    
    input()
    speaking(string)
    input()
    
    
    
os.system(convert_to_pdf(page_number))    

