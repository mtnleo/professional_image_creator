import folder_handling as fh
from PIL import Image
from rembg import remove
import os

class edited_image:
    image = Image.Image
    size = ( )

    def __init__(self, image, size=Image.Image.size, path=os.getcwd()):
        self.image = image
        self.size = size
        self.path = path
        self.folder_handler = fh.FolderHandling(self.path)
    
    def remove_background(self):
        removed_img = remove(self.image)
        rotated_img = removed_img.transpose(2)
        rotated_img.save(self.folder_handler.get_edited_pictures_folder() + self.folder_handler.get_output_name_new_image())
        

    


if __name__ == "__main__":
    new_image = edited_image(Image.open("normal_bg.jpg"))
    new_image.remove_background()