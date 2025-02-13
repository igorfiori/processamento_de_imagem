from skimage.io import imread, imsave
from skimage.color import imread, imsave

def read_image(path, as_gray=False):
    image = imread(path, as_gray=as_gray)
    return image

def save_image(image, path):
    imsave(path, image)
    return None