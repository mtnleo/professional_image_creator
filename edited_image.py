import folder_handling as fh
from PIL import Image
from rembg import remove
import os
import random

class edited_image:
    image = Image.Image
    size = ( )

    def __init__(self, image, size=Image.Image.size, path=os.getcwd()):
        self.image = image
        self.size = size
        self.path = path
        self.folder_handler = fh.FolderHandling(self.path)
    
    def remove_background_and_save(self):
        removed_img = remove(self.image)
        removed_img.save(self.folder_handler.get_edited_pictures_folder() + self.folder_handler.get_output_name_new_image())

        return removed_img

    def remove_background(self):
        removed_img = remove(self.image)

        return removed_img
        
    def edit_all_pictures_from_folder(path=os.getcwd()):
        new_fh = fh.FolderHandling(path)
        unedited_path = new_fh.get_unedited_pictures_folder()

        dir_list = os.listdir(unedited_path)

        if dir_list:
            for file in os.listdir(unedited_path):
                im = edited_image(Image.open(unedited_path + f"\\{file}"))
                im._merge_headshot_and_background()
        else:
            print(f"The folder is empty!\nFolder path: {unedited_path}")
            return False

    def remove_background_for_all_folder(path=os.getcwd()):
        new_fh = fh.FolderHandling(path)
        unedited_path = new_fh.get_unedited_pictures_folder()

        dir_list = os.listdir(unedited_path)

        if dir_list:
            for file in os.listdir(unedited_path):
                im = edited_image(Image.open(unedited_path + f"\\{file}"))
                im.remove_background_and_save()
        else:
            print(f"The folder is empty!\nFolder path: {unedited_path}")
            return False

    def _get_background_image_path(self): # picks a random background every time
        background_folder_path = self.folder_handler.get_background_folder()
        random_image_path = ""
        try:
            random_image_path = background_folder_path + "\\" + random.choice(os.listdir(background_folder_path))
        except:
            print("Error retrieving the background image")

        return random_image_path

    def _resize_images(self, background):
        headshot_size = self.image.size
        background_size = background.size

        new_size = [0, 0]
        if headshot_size[0] < background_size[0]:
            new_size[0] = headshot_size[0]
        else:
            new_size[0] = background_size[0]
        
        if headshot_size[1] < background_size[1]:
            new_size[1] = headshot_size[1]
        else:
            new_size[1] = background_size[1]

        resized_headshot = self.image.resize(size=tuple(new_size))
        resized_background = background.resize(size=tuple(new_size))

        return resized_headshot, resized_background


    def _merge_headshot_and_background(self):
        self.image = self.remove_background()

        background_path = self._get_background_image_path()
        background = Image.open(background_path)

        resized_headshot, resized_background = self._resize_images(background)
        resized_headshot = resized_headshot.convert(mode="RGBA")
        resized_background = resized_background.convert(mode="RGBA")

        # merging background + headshot image
        merged_image = Image.alpha_composite(resized_background, resized_headshot)

        merged_image.save(self.folder_handler.get_edited_pictures_folder() + self.folder_handler.get_output_name_new_image())

        return merged_image

    def create_headshot(self, all_folder = False): #if no image path/image is given, it'll edit all images in the /unedited_images dir
        if all_folder:
            self.edit_all_pictures_from_folder()
        else:
            try:
                return self._merge_headshot_and_background()
                
            except:
                print("Error trying to load the image.")

    def resize_image_user(self, new_width, new_height):
        size = [new_width, new_height]
        
        resized_image = self.image.resize(size=tuple(size))
        resized_image.save(self.folder_handler.get_edited_pictures_folder() + self.folder_handler.get_output_name_new_image())

        return resized_image

