from distutils import extension
import os
from pickletools import optimize
from PIL import Image

import os

from pkg_resources import working_set

downloadsFolder = "Raiz:/path/path/"
picturesFolder = "Raiz:path/path/compressed/"

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".jpg", "*jpeg", ".png"]:
            picture = Image.open(downloadsFolder + filename)
            picture.save(picturesFolder + "comprimido_"+filename, optimize = True, quality=60)
            os.remove(downloadsFolder + filename)
            print(name + ": " + extension)
        
        if extension in [".mp4"]:
            musicFolder = "Raiz:/path/path/path/"
            os.rename(downloadsFolder + filename, musicFolder + filename)