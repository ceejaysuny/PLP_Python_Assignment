
def file_read_write():
    try:
        # Ask the user for the input filename
        input_file = input("Enter the name of the file to read: ")
        
        # Try opening the file for reading
        file = open(input_file, 'r')
        content = file.readlines()
        file.close()
        
        # Modify the content (for example, add line numbers)
        modified_content = [f"{i + 1}: {line}" for i, line in enumerate(content)]
        
        # Ask the user for the output filename
        output_file = input("Enter the name of the file to write the modified content: ")
        
        # Write the modified content to a new file
        file = open(output_file, 'w')
        file.writelines(modified_content)
        file.close()
        
        print(f"Modified content has been written to '{output_file}' successfully.")
    
    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: Permission denied. You may not have the right access to read/write the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function
file_read_write()
