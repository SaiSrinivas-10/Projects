# # Before running this code, do these
# # pip install opencv-python 
# # pip install pyzbar
# If there is an error while importing pyzbar, update Visual C++ and restart the IDE/Text Editor
# Later add items in the dictionary named data

# from os import name
import cv2
from pyzbar.pyzbar import decode

# Add items here
data = {'8198495135207': 'Book'}

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,460)
cart = []

camera = True
while camera == True:
    success,frame = cap.read()

    
    for code in decode(frame):
        if(code.data.decode('utf-8') not in cart):   
            decodedcode = code.data.decode('utf-8')    
            print(decodedcode)
            cart.append(decodedcode)
            quantity = int(input("Enter the quantity :"))
            if(decodedcode in data.keys()):
                print("Item: {}   Quantity : {}".format(data[decodedcode],quantity))
            else:
                print("Error")
    cv2.imshow('Capturing video',frame)
    cv2.waitKey(1)
