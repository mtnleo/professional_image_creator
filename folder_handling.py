import os

class FolderHandling:
    unedited_folder_name = "\\unedited_images"
    edited_folder_name = "\\edited_images"
    background_folder_name = "\\background"
    removed_bg_folder_name = "\\removed_background"
    headshot_folder_name = "\\headshots"
    resized_folder_name = "\\resized"

    def __init__(self, path=os.getcwd()):
        self.path = path

    def make_backslash_double(path):
        path = path.replace("\\", "\\\\")
        return path

    def get_unedited_pictures_folder(self):
        folder_name_path = self.path + FolderHandling.unedited_folder_name
        if os.path.exists(folder_name_path) == False:
            os.makedirs(folder_name_path)

        return folder_name_path

    def get_edited_pictures_folder(self):
        folder_name_path = self.path + FolderHandling.edited_folder_name
        if os.path.exists(folder_name_path) == False:
            os.makedirs(folder_name_path)

        return folder_name_path

    def get_removed_bg_folder(self):
        rembg_path = self.get_edited_pictures_folder() + self.removed_bg_folder_name
        if os.path.exists(rembg_path) == False:
            os.makedirs(rembg_path)

        return rembg_path

    def get_edited_headshots_folder(self):
        headshots_path = self.get_edited_pictures_folder() + self.headshot_folder_name
        if os.path.exists(headshots_path) == False:
            os.makedirs(headshots_path)

        return headshots_path

    def get_resized_pictures_folder(self):
        resized_path = self.get_edited_pictures_folder() + self.resized_folder_name
        if os.path.exists(resized_path) == False:
            os.makedirs(resized_path)

        return resized_path


    def get_background_folder(self):
        background_folder = self.path + self.background_folder_name
        if os.path.exists(background_folder) == False: # if it doesn't exists, it'll have to be refilled with images
            os.makedirs(background_folder)

        return background_folder

    def get_output_name_new_image(self, path = ""):
        if path == "":
            path = self.get_edited_pictures_folder()
            
        image_list = os.listdir(path)
        return "\\edited_" + str(len(image_list)) + ".png"




if __name__ == "__main__":
    folder = FolderHandling("D:\Programming\Python\Image Processing")
    path = folder.get_unedited_pictures_folder()
    print(path)
    path = folder.get_edited_pictures_folder()
    print(path)
