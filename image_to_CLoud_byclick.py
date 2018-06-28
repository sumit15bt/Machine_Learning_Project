import os
import cv2
import random
camera = cv2.VideoCapture(0)

#print("press c to capture image ")
#press 'c' to capture image 
while camera.isOpened():
    frame=camera.read()[1]
    cv2.imshow("image clicked",frame)
    if cv2.waitKey(2) &  0xFF==ord('c'):
        cv2.imshow("image clicked",frame)
        x=random.random()
        y=str(x)[2:5]
	# saves image to current folder,It may be not required
        cv2.imwrite('Clicked_image'+y+'.jpg',frame)
	#saves photo cloud from the current folder
        os.system("sshpass -p krishna scp  /home/ss/Desktop/Clicked_image"+y+".jpg krishna@18.191.129.15:")
        
    elif cv2.waitKey(1) &  0xFF==ord('q'):
        break

cv2.destroyAllWindows()
camera.release()
