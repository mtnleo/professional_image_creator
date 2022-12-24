import os

class FolderHandling:
    unedited_folder_name = "\\unedited_images"
    edited_folder_name = "\\edited_images"
    background_folder_name = "\\background"

    def __init__(self, path=os.getcwd()):
        self.path = path

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


    def get_background_folder(self):
        background_folder = self.path + self.background_folder_name
        if os.path.exists(background_folder) == False: # if it doesn't exists, it'll have to be refilled with images
            os.makedirs(background_folder)

        return background_folder

    def get_output_name_new_image(self):
        image_list = os.listdir(self.get_edited_pictures_folder())
        return "\\edited_" + str(len(image_list)) + ".png"




if __name__ == "__main__":
    folder = FolderHandling("D:\Programming\Python\Image Processing")
    path = folder.get_unedited_pictures_folder()
    print(path)
    path = folder.get_edited_pictures_folder()
    print(path)
