import edited_image as em
import os
import folder_handling as fh
import time

def print_menu():
    print("----------------------- IMAGE PROCESSING -----------------------\n")
    print("| 1 |   Remove background from an image")
    print("| 2 |   Remove background for each image in the 'unedited_images' folder")
    print("| 3 |   Create a professional headshot from an image")
    print("| 4 |   Create a professional headshot for each image in the 'unedited_images' folder")
    print("| 5 |   Help & How to use")
    print("| 6 |   Exit")

if __name__ == "__main__":
    cont = True
    success = True
    while cont == True:
        os.system("cls")
        print_menu()
        option = int(input("\nChoose an option: "))

        if option == 1:
            image_path = (input("Paste here your image's path (Shift + Ins.): "))
            image_path = fh.FolderHandling.make_backslash_double(image_path)
            
            print("--> Removing background now...")
            im = em.edited_image(em.Image.open(image_path))
            im.remove_background_and_save()
            print(f"--> Background removed!\nCheck '{im.folder_handler.get_edited_pictures_folder()}'")

        elif option == 2:
            print("--> Removing background for all images in the folder, this might take a while...")
            success = em.edited_image.remove_background_for_all_folder()
            if success:
                print("--> Backgrounds removed!\nCheck your 'edited_images' folder")

        elif option == 3:
            image_path = (input("Paste here your image's path (Shift + Ins.): "))
            image_path = fh.FolderHandling.make_backslash_double(image_path)
            im = em.edited_image(em.Image.open(image_path))

            print(f"--> Editing image now...")
            im.create_headshot()
            print(f"--> Headshot created!\nCheck '{im.folder_handler.get_edited_pictures_folder()}'")

        elif option == 4:
            print("--> Editing images from the folder, this might take a while...")
            success = em.edited_image.edit_all_pictures_from_folder()
            if success:
                print("--> Images edited!\nCheck your 'edited_images' folder")

        elif option == 5:
            print("Welcome to the Image Processing CLI!")
            print("For converting or editing images, you may indicate the path in your computer")
            print("You can do that by right-clicking the image, and clicking 'Copy Path'")
            print("You can also save the pictures you want to get edited into the")
            print("'unedited_images' folder, and then selecting the options that")
            print("edit a whole folder at once. Creating copies of the unedited photos")

        elif option == 6:
            print("Goodbye!")
            cont = False

        else:
            print("| X | INCORRECT OPTION, TRY AGAIN | X |")
        
        os.system("pause")




