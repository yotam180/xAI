import numpy as np 
import nLib
import vision
import google_images
import os

google = google_images.GoogleSearch()

def get_images(query, min_amount, folder):
    global google

    if not os.path.exists(folder):
        os.makedirs(folder)

    entries = google.search(query, min_amount)
    for i, e in enumerate(entries):
        vision.save_image(vision.download_image(e["tu"]), folder + "/_" + str(i) + ".jpg")
        print "%d of %d entries saved" % (i + 1, len(entries))

def make_network(p_folder, n_folder):
    positives = os.listdir(p_folder)
    negatives = os.listdir(n_folder)

    training_data = []
    test_data = []

    for i, p in enumerate(positives):
        img = vision.load_image(p_folder + "/" + p)
        (test_data if i < 50 else training_data).append((vision.resize(vision.center_square(img)).reshape(-1, 1) / 256.0, np.array([[1.0], [0.0]])))

    for i, n in enumerate(negatives):
        img = vision.load_image(n_folder + "/" + n)
        (test_data if i < 50 else training_data).append((vision.resize(vision.center_square(img)).reshape(-1, 1) / 256.0, np.array([[0.0], [1.0]])))
    print training_data[0][0].shape
    net = nLib.CNN([2500, 512, 30, 2], 2.0)
    net.train(training_data, 100, 20, test_data, test)

def test(p, w):
    print "Wanted %d received %f,%f" % (np.argmax(w), p[0][0], p[1][0])
    return np.argmax(p) == np.argmax(w)

#make_network("dogs", "buildings")
get_images("eggs", 300, "eggs")
