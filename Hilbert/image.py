import numpy as np
from PIL import Image

def scaleForRank(rank):
    im = Image.open('kolala.jpg').convert('L')
    width, height = im.size   # Get dimensions

    new_width = 450
    new_height = 450

    left = (width - new_width)/2
    top = (height - new_height)/2
    right = (width + new_width)/2
    bottom = (height + new_height)/2

    # Crop the center of the image
    im = im.crop((left, top, right, bottom)).resize((rank, rank))
    im = np.array(im) #you can pass multiple arguments in single line
    return im
