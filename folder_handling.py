import os

class FolderHandling:
    unedited_folder_name = "\\unedited_images"
    edited_folder_name = "\\edited_images"
    background_folder_name = "\\background"
    removed_bg_folder_name = "\\edited_images\\removed_background"
    headshot_folder_name = "\\edited_images\\headshots"
    resized_folder_name = "\\edited_images\\resized"

    def __init__(self, path=os.getcwd()):
        self.path = path

    def make_backslash_double(path):
        path = path.replace("\\", "\\\\")
        return path

    def get_pictures_folder(self, path_of_folder):
        folder_name_path = self.path + path_of_folder
        if os.path.exists(folder_name_path) == False:
            os.makedirs(folder_name_path)

        return folder_name_path

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
