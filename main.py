# coding=utf-8
# Fast Fourrier Transform image compression

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

from FFT_threshold import FFT_threshold
from OCR import OCR, OCR_accuracy

def main(image):
    fig, axs = plt.subplots(1, 4)
    for enum, level in enumerate([1, 0.5, 0.1, 0.05]):
        img = Image.open(image).convert("L")  # read RGB image into greyscale
        #img = np.mean(img, -1)  # convert to greyscale

        comp_img = FFT_threshold(img, level)

        axs[enum].imshow(comp_img)

        im = Image.fromarray(comp_img)
        im.convert("RGB").save("img1.png")
        axs[enum].title.set_text(str(level*100) + "% compression size - "+ str(round(OCR_accuracy(str(OCR("text.png")), str(OCR("img1.png"))), 3)*100) + " % read")
    plt.show()

if __name__ == '__main__':
    main("text.png")



