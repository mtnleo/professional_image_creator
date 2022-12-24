import edited_image as em
import os
import folder_handling as fh
import time

def print_menu():
    print("----------------------- IMAGE PROCESSING -----------------------\n")
    print("| 1 |   Remove background from an image")
    print("| 2 |   Create a professional headshot from an image")
    print("| 3 |   Create a professional headshot for each image in the 'unedited_images' folder")
    print("| 4 |   Exit")

if __name__ == "__main__":
    cont = True
    while cont == True:
        os.system("cls")
        print_menu()
        option = int(input("\nChoose an option: "))

        if option == 1:
            image_path = (input("Paste here your image's path: "))
            image_path = fh.FolderHandling.make_backslash_double(image_path)
            
            print("--> Removing background now...")
            im = em.edited_image(em.Image.open(image_path))
            im.remove_background_and_save()
            print(f"--> Background removed!\nCheck '{im.folder_handler.get_edited_pictures_folder}'")

        elif option == 2:
            image_path = (input("Paste here your image's path: "))
            image_path = fh.FolderHandling.make_backslash_double(image_path)
            im = em.edited_image(em.Image.open(image_path))

            print(f"--> Editing image now...")
            im.create_headshot()
            print(f"--> Headshot created!\nCheck '{im.folder_handler.get_edited_pictures_folder}'")

        elif option == 3:
            print("--> Editing images from the folder, this might take a while...")
            em.edited_image.edit_all_pictures_from_folder()
            print("--> Images edited!\nCheck your 'edited_images' folder")

        elif option == 4:
            print("Goodbye!")
            cont = False

        else:
            print("| X | INCORRECT OPTION, TRY AGAIN | X |")
        
        time.sleep(5)




