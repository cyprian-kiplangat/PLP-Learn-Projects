def read_and_modify_file():
    """
    Read content from a user-specified file, modify it, and write to a new file.
    Handles various file operation errors gracefully.
    """
    # Get input filename from user
    input_filename = input("Enter the name of the file to read: ")
    
    try:
        # Attempt to open and read the input file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
            print(f"Successfully read file: {input_filename}")
            print(f"Original content length: {len(content)} characters")
            
            # Modify the content (example: convert to uppercase)
            modified_content = content.upper()
            
            # Get output filename
            output_filename = input("Enter the name of the file to write to: ")
            
            try:
                # Write modified content to output file
                with open(output_filename, 'w') as output_file:
                    output_file.write(modified_content)
                    print(f"Successfully wrote modified content to: {output_filename}")
                    print(f"Modified content length: {len(modified_content)} characters")
            
            except IOError as write_error:
                print(f"Error writing to file '{output_filename}': {write_error}")
            except Exception as e:
                print(f"Unexpected error during write operation: {e}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: You don't have permission to access '{input_filename}'.")
    except IOError as read_error:
        print(f"Error reading file '{input_filename}': {read_error}")
    except UnicodeDecodeError:
        print(f"Error: Cannot decode file '{input_filename}'. It might be a binary file.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    print("File Read & Write Program with Error Handling")
    print("---------------------------------------------")
    read_and_modify_file()