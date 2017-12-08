import nLib
import cv2
import numpy as np

net = nLib.define_network_model("dog")
net.load("checkpoints/dog9595")

while True:
    u = input("Enter file path: ")

    img = cv2.imread(u, cv2.IMREAD_GRAYSCALE)

    res = net.predict(img.reshape(-1, nLib.IMG_SIZE, nLib.IMG_SIZE, 1))

    print(["Not dog", "Dog"][np.argmax(res)])
    print (str(np.max(res) * 100.0 / np.sum(res)) + "%")