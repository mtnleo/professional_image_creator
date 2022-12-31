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
    print("| 5 |   Resize an image")
    print("| 6 |   Help & How to use")
    print("| 7 |   Exit")

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
            print(f"--> Background removed!\nCheck '{im.folder_handler.get_removed_bg_folder()}'")

        elif option == 2:
            print("--> Removing background for all images in the folder, this might take a while...")
            success = em.edited_image.remove_background_for_all_folder()
            if success:
                print("--> Backgrounds removed!\nCheck 'edited_images/removed_background'")

        elif option == 3:
            image_path = (input("Paste here your image's path (Shift + Ins.): "))
            image_path = fh.FolderHandling.make_backslash_double(image_path)
            im = em.edited_image(em.Image.open(image_path))

            print(f"--> Editing image now...")
            im.create_headshot()
            print(f"--> Headshot created!\nCheck '{im.folder_handler.get_edited_headshots_folder()}'")

        elif option == 4:
            print("--> Editing images from the folder, this might take a while...")
            success = em.edited_image.headshot_all_pictures_from_folder()
            if success:
                print(f"--> Headshots created!\nCheck 'edited_images/headshots''")

        elif option == 5:
            image_path = (input("Paste here your image's path (Shift + Ins.): "))
            image_path = fh.FolderHandling.make_backslash_double(image_path)
            im = em.edited_image(em.Image.open(image_path)) 

            new_width = int(input("New Width -> "))
            new_height = int(input("New Height -> "))

            print(f"--> Resizing image now...")
            try:
                im.resize_image_user(new_width, new_height)
                print(f"--> Image resized!\nCheck '{im.folder_handler.get_resized_pictures_folder()}'")
            except:
                print("Error trying to resize the image, try again")

        elif option == 6:
            print("Welcome to the Image Processing CLI!")
            print("For converting or editing images, you may indicate the path in your computer")
            print("You can do that by right-clicking the image, and clicking 'Copy Path'")
            print("You can also save the pictures you want to get edited into the")
            print("'unedited_images' folder, and then selecting the options that")
            print("edit a whole folder at once. Creating copies of the unedited photos")

        elif option == 7:
            print("Goodbye!")
            cont = False

        else:
            print("| X | INCORRECT OPTION, TRY AGAIN | X |")
        
        os.system("pause")




