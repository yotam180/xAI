import mnist_loader
import nLib
import numpy as np
import cv2

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

net = nLib.CNN([784, 30, 10], 3.0)
net.train(training_data, 30, 10, test_data, lambda p, w: np.argmax(p) == w)

# net = nlib.cnn("network.net")

# digits = cv2.imread("digits.png", cv2.imread_grayscale)

# _, thresh = cv2.threshold(digits, 127, 255, 0)

# _, cnts, _ = cv2.findcontours(thresh, cv2.retr_tree, cv2.chain_approx_simple)

# rects = []

# for c in cnts:
    # b = cv2.boundingrect(c)
    
    # if b[2] < 30 or b[3] < 30 or b[2] > digits.shape[0] * 0.9 or b[3] > digits.shape[1] * 0.9:
        # continue
    # #print b
    # if any([(abs(x[0] - b[0]) < 20 and abs(x[1] - b[1]) < 20) for x in rects]):
        # continue
    # i = digits[b[1]:b[1]+b[3], b[0]:b[0]+b[2]]
    # rects.append(b)

    # j = 1 - cv2.resize(i, (28, 28)).flatten().reshape(-1, 1) / 256.0
    # print np.mean(j)
    
    # #print net.sizes[0]
    # #print 1 - cv2.resize(i, (28, 28)).flatten().reshape(-1, 1) / 256.0
    # print np.argmax(net.predict(j))

    # cv2.imshow("w", 1 - cv2.resize(i.astype("float32"), (28, 28)) / 256.0)
    # cv2.waitkey(0)
    # cv2.destroyallwindows()

