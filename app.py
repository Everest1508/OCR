from flask import Flask,render_template, request,send_file
from werkzeug.utils import secure_filename
import cv2
# import pytesseract as tess
import numpy as np
import os
from text_to_img import convertToImg
# tess.pytesseract.tesseract_cmd=r'.\Tesseract-OCR\tesseract.exe'
import easyocr
reader = easyocr.Reader(['en'])

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods=["POST"])
def upload_file():
    # print(request.form.get('textarea'))
    uploaded_file = request.files['file']
    charset=True
    # print(len(uploaded_file.filename))
    if uploaded_file.filename != '':
        for i in uploaded_file.filename:
            if i in ('_','-','(',')','}','{','[',']',';',':','/'):
                charset=False
        if charset==False:
            return render_template("index.html",mesg="The File contains Symbols please rename it!")
        else:        
            uploaded_file.save(secure_filename(uploaded_file.filename))
            img = cv2.imread(uploaded_file.filename)
            # gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            # gray, img_bin = cv2.threshold(gray,128,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            # gray = cv2.bitwise_not(img_bin)
            # kernel = np.ones((2, 1), np.uint8)
            # img = cv2.erode(gray, kernel, iterations=1)
            # img = cv2.dilate(img, kernel, iterations=1)
            results = reader.readtext(img)
            out_below = " ".join([x[1] for x in results])
            # out_below = tess.image_to_string(img)
            os.remove(uploaded_file.filename)
            # print("OUTPUT:", out_below)
            return render_template("index.html",mesg=out_below)
    if uploaded_file.filename == '' and request.form.get('textarea') !='':
        convertToImg(request.form.get('textarea'))
        return send_file("output.png", as_attachment=True)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)