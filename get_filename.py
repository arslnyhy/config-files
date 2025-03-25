import os

def gather_filenames(directory, output_file):
    try:
        # Get a list of files in the specified directory
        filenames = [os.path.splitext(file)[0] for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
        
        # Write the filenames to the output file
        with open(output_file, 'w') as f:
            for filename in filenames:
                f.write(f"{filename}\n")
        
        print(f"File names written to {output_file} successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Specify the directory and output file path
    directory = input("Enter the path of the directory: ").strip()
    output_file = input("Enter the path for the output text file: ").strip()
    
    gather_filenames(directory, output_file)
