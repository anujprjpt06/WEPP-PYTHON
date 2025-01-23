#   "C:\\Users\\anujp\\AppData\\Local\\Programs\\Python\\Python312\\text.txt"


def Display_Modes():
    print("File Handling Options:")
    print("1. Read from file")
    print("2. Write to file")
    print("3. Search in file")
    print("4. Exit")

def Read_File():
    try:
        with open("C:\\Users\\anujp\\AppData\\Local\\Programs\\Python\\Python312\\text.txt", 'r') as file:
            content = file.read()
            print("\nFile Content:\n", content)
    except FileNotFoundError:
        print("\nFile not found.\n")
        #file.close()

def Write_File():
    content = input("Enter content to write into the file: ")
    with open("C:\\Users\\anujp\\AppData\\Local\\Programs\\Python\\Python312\\text.txt", 'a') as file:  
        file.write(content + '\n')
    print("\nContent appended to file.\n")

def Search_File():
    search_term = input("Enter the word to search for: ")
    try:
        with open("C:\\Users\\anujp\\AppData\\Local\\Programs\\Python\\Python312\\text.txt", 'r') as file:
            content = file.read()
            if search_term in content:
                print(f"\n'{search_term}' found in the file.\n")
            else:
                print(f"\n'{search_term}' not found in the file.\n")
    except FileNotFoundError:
        print("\nFile not found.\n")

def main():
    while True:
        Display_Modes()
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            Read_File()
        elif choice == '2':
            Write_File()
        elif choice == '3':
            Search_File()
        elif choice == '4':
            print("\nExiting program.\n")
            break
        else:
            print("\nInvalid choice. Please try again.\n")


main()





