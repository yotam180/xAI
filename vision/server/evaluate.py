import nLib
import cv2

net = nLib.define_network_model()
net.load("models/cat")

u = input("Enter file path: ")

img = cv2.imread(u, cv2.IMREAD_GRAYSCALE)

print(net.predict(img.reshape(None, nLib.IMG_SIZE, nLib.IMG_SIZE, 1)))