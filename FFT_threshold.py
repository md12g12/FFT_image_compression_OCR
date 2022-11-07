# coding=utf-8
# Fast Fourrier Transform image compression

import numpy as np


def FFT_threshold(img, level):

    Bt = np.fft.fft2(img) #take Fast Fourier Transform
    Btsort = np.sort(np.abs(Bt.reshape(-1)))
    thresh = Btsort[int(np.floor((1-level*len(Btsort))))]
    ind = np.abs(Bt)>thresh
    Atlow = Bt * ind
    Alow = np.fft.ifft2(Atlow).real
    return(Alow)


if __name__ == '__main__':
    FFT_threshold("test_image.png", 0.001)

