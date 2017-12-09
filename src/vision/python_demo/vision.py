import cv2
import urllib
import numpy as np
import nLib

from random import randint

def download_image(url):
    req = urllib.urlopen(url)
    nparr = np.array(bytearray(req.read()), dtype="uint8")
    return cv2.imdecode(nparr, cv2.IMREAD_COLOR)

def center_square(img):
    h = img.shape[0]
    w = img.shape[1]
    return img[(h - min(w, h)) / 2: (h + min(w, h)) / 2, (w - min(w, h)) / 2: (w + min(w, h)) / 2]

def random_square(img):
    h = img.shape[0]
    w = img.shape[1]
    m = min(w, h)
    x = randint(0, w - m)
    y = randint(0, h - m)
    return img[y: y+m, x:x+m]

def resize(img):
    return cv2.resize(img, (50, 50))

def save_image(img, file):
    cv2.imwrite(file, img)

def load_image(file):
    return cv2.imread(file, cv2.IMREAD_GRAYSCALE)