import numpy as np
import cv2

def main():
    face_cascade = cv2.CascadeClassifier('C:\\Users\\MOHNISH REDDY\\Anaconda3\\Library\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
        
    while ret:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #cv2.imshow("faces", gray)
        faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.3, minNeighbors = 5)
        #print(faces)
        for (x, y, w, h) in faces:
            frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
        cv2.imshow('faces', frame)
        if cv2.waitKey(1) == 27:
            break
        
    cv2.destroyAllWindows()
    cap.release()

if __name__ == "__main__":
    main()