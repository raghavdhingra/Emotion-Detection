# from keras.models import load_model
# classifier = load_model('model.hdf5')

# dictclass = {'Angry': 0, 'Sad': 5, 'Neutral': 4, 'Disgust': 1, 'Surprise': 6, 'Fear': 2, 'Happy': 3}
# class_labels = {v: k for k, v in dictclass.items()}


from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
import os
import re
from keras.preprocessing.image import img_to_array
import cv2
import base64
import numpy as np
from main.emo_capt import face_detector
import main.emo_capt
from main.emo_capt import classifier, dictclass, class_labels, face_classifier
# face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

dataUrlPattern = re.compile('data:image/(png|jpeg);base64,(.*)$')

# Create your views here.
def home(request):
    context = {
        "title":"CaptureCam | Home",
    }
    return render(request,'index.html',context)


def captureImage(request):
    # dict = {}
    context = {
        "title":"HOME",
    }
    if request.FILES:
        image = request.FILES['image']
        print(image)
        # img = cv2.imread(image)
        img = cv2.imdecode(np.fromstring(image.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        rects, faces, image = face_detector(img)
        i = 0
        for face in faces:
            print(face.shape)
            print(face)
            roi = face.astype("float") / 255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)

            # make a prediction on the ROI, then lookup the class
            preds = classifier.predict(roi)[0]
            label = class_labels[preds.argmax()]   

            #Overlay our detected emotion on our pic
            label_position = (rects[i][0] + int((rects[i][1]/2)), abs(rects[i][2] - 10))
            i =+ 1
            cv2.putText(image, label, label_position , cv2.FONT_HERSHEY_SIMPLEX,1, (0,255,0), 2)            
        # cv2.imshow("Emotion Detector", image)
        cv2.imwrite(os.path.join('static', 'result.jpg'),image)
        # print(image)
        context = {
            "title":"HOME",
            # "image":"/result.jpg",
        }
        # cv2.waitKey(0)

        # cv2.destroyAllWindows()

    return render(request,'result.html',context)