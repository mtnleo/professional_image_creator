from PIL import Image
from rembg import remove
import os

class edited_image:
    image = Image.Image
    size = ( )
    output_path = os.getcwd() + "\\removed_bg.png"

    def __init__(self, image, size=Image.Image.size):
        self.image = image
        self.size = size
    
    def remove_background(self):
        removed_img = remove(self.image)
        removed_img.save(edited_image.output_path)


if __name__ == "__main__":
    new_image = edited_image(Image.open("normal_bg.jpg"))
    new_image.remove_background()