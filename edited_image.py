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
        removed_img.save(self.folder_handler.get_edited_pictures_folder() + self.folder_handler.get_output_name_new_image())
        
    def get_all_pictures_from_folder(path=os.getcwd()):
        new_fh = fh.FolderHandling(path)
        unedited_path = new_fh.get_unedited_pictures_folder()
        for file in os.listdir(unedited_path):
            im = edited_image(Image.open(unedited_path + f"\\{file}"))
            im.remove_background()


if __name__ == "__main__":
    edited_image.get_all_pictures_from_folder()