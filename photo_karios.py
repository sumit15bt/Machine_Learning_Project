#!/usr/bin/env python2
import urllib.request
import cv2
import os
import random
import json

cap=cv2.VideoCapture(0)
while cap.isOpened():
    status,img=cap.read()
    cv2.imshow("Press C for 2 sec to capture the photo",img)
    if  cv2.waitKey(1) & 0xff==ord('c'):
        cv2.imshow("Capture Image",img)
        num=str(random.random())[2:6]
        print(num)
        cv2.imwrite("./static/Uploaded_Images/Image"+num+".jpg",img)
        result=os.system('sshpass -p krishna scp ./static/Uploaded_Images/Image'+num+'.jpg krishna@13.58.227.240:')
        print("Image Succesfully send")
        url="http://13.58.227.240/images/Image"+num+".jpg"
        values = '''
       	{
        "image": "'''+url+'''", 
        "subject_id": "SUMIT",
        "gallery_name": "MyGallery"
        }'''
        headers = {
        'Content-Type': 'application/json',
        'app_id': 'd0ab0d68',
        'app_key': '2bd95d461d67d91c7c309aa13c79a4cf'
        }
        request = urllib.request.Request('https://api.kairos.com/enroll', data=values, headers=headers)
        print(request)
        response_body = urllib.request.urlopen(request).read()
        cont = json.loads(response_body.decode('utf-8'))
        print(cont)
        break
cv2.destroyAllWindows()
cap.release()
