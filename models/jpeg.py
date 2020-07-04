import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from scipy import fftpack


def get_image(raw):
    img = raw.clip(0, 255)
    img = img.astype('uint8')
    img = Image.fromarray(img)
    return img


def image_to_array(file):
    image = Image.open(file)
    gray = image.convert('L')
    return np.array(gray, dtype=float)


def dct2(matrix):
    return fftpack.dct(fftpack.dct(matrix, norm='ortho', axis=0), norm='ortho', axis=1)


def idct2(matrix):
    return fftpack.idct(fftpack.idct(matrix, norm='ortho', axis=0), norm='ortho', axis=1)


def display_images(image, d, f):
    # se f,d non sono convertibili in int

    img = image_to_array(image)
    x_size = img.shape[0]
    y_size = img.shape[1]

    f = int(max(f))
    d = int(max(d))
    if 1 <= f <= x_size and f <= y_size and 0 <= d <= (2 * f - 2):

        recon_img = np.zeros(img.shape)

        for i in list(range(0, x_size, f)):
            for j in list(range(0, x_size, f)):

                if i + f > x_size or j + f > y_size:
                    continue

                dct = dct2(img[i:i + f, j:j + f])

                (ck, cl) = np.indices((f, f))
                index = ck + cl >= d
                dct[index] = 0

                idct = idct2(dct)

                recon_img[i:i + f, j:j + f] = idct

        recon_img = get_image(recon_img)

        plt.figure()
        plt.imshow(recon_img, cmap='gray', vmax=255, vmin=0)
        plt.show()


if __name__ == "__main__":
    pass
