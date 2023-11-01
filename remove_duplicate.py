from main import *

# Remove the duplicate rows
def remove_duplicate(data) -> None:
    pass 

def main():
    # get all the arguments from the command line
    arguments = parse_cmd()
    # parsing the arguments
    filename = arguments[0].split('=')[1]  
    filename_out = arguments[1].split('=')[1]
    # Load the data from the file
    data = read_file(filename)   
    # remove the duplicate rows and save the result to the output file   
    remove_duplicate(data)
    create_csv_file(filename_out, data)
    
if __name__ == '__main__':
    main()
