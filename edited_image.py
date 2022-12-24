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
        for file in os.listdir(unedited_path):
            im = edited_image(Image.open(unedited_path + f"\\{file}"))
            im._merge_headshot_and_background()

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

    def create_headshot(image_path = " ", image = None): #if no image path/image is given, it'll edit all images in the /unedited_images dir
        if image_path == " " and image == None:
            print("Image path not given.\nEditing all images in /unedited_images")
            edited_image.edit_all_pictures_from_folder()
        else:
            if image != None:
                im = edited_image(image)
                im._merge_headshot_and_background()

                return im
            else:
                try:
                    im = edited_image(Image.open(image_path))
                    im._merge_headshot_and_background()

                    return im
                except:
                    print("Error trying to load the image.")



if __name__ == "__main__":
    edited_image.create_headshot("D:\\Programming\\Python\\Image Processing\\unedited_images\\shoot-me-now-acting-agency-headshot.jpg")