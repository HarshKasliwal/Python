def print_details_of_file(file_content): 
    '''function to find details of the file'''

    line_count, word_count, char_count = 0, 0, 0
     # To find no of lines
    line_list = file_content.split("\n")
    line_count = len(line_list)


    # To find no of words 
    for line in line_list:
        word_list = line.split()
        word_count += len(word_list)

# To find number of chars 
    char_count = len(file_content)
    print("The file content:\n" + ("-" * 30) + f"\n{file_content}\n" + ("-" * 30))
    print(f"Line Count :\t {line_count}") 
    print(f"Word Count :\t {word_count}") 
    print(f"Char Count :\t {char_count}")
with open("useless.txt", 'r') as f: 
    file_content = f.read()
    print_details_of_file(file_content)
