import os

def get_folder_names(directory):
    try:
        # Get the list of all files and directories
        dir_list = os.listdir(directory)
        
        # Filter out only directories
        folders = [name for name in dir_list if os.path.isdir(os.path.join(directory, name))]
        
        # Write the folder names to a text file
        with open('/home/user/folder_names.txt', 'w') as file:
            for folder in folders:
                file.write(f"{folder}\n")
                
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the directory
directory = '/home/user/mockit/configs/'

# Call the function
get_folder_names(directory)
