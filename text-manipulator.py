#uppercase function
def text_uppercase(text):
    return text.upper()

#lowercase function 
def text_lowercase(text):
    return text.lower()

#Capitalcase function
def text_capitalcase(text):
    return text.capitalize()

#Count characters function
def text_count(text):
    return len(text)

#word count function
def word_count(text):
    words = text.split()
    count = len(words)
    return count

#remove extra spaces
def remove_extra_spaces(text):
    return text.strip()

#reverse text
def reverse_text(text):
    return text[::-1]

#find alpha numeric
def find_alphanum(text):
    return text.isalnum()

#text ends with
def text_endswith(text, word):
    return text.endswith(word)

#center align
def center_align(text, width):
    return text.center(width)

#count occurance
def count_occurance(text, word):
    return text.count(word)

#find index
def find_index(text, word):
    return text.index(word)

#perform split
def perform_split(text, separator):
    return text.split(separator)

#perform partition
def perform_partition(text, partition):
    return text.partition(partition)

#perform replace
def perform_replace(text, oldval, newval):
    return text.replace(oldval, newval)

def text_manipulator():
    text = input("Enter your text:")

    while True:
        print("\n TEXT MANIPULATOR ")
        print("1. Convert text to Uppercase")
        print("2. Convert to Lowercase")
        print("3. Convert to Capital Case")
        print("4. Count Characters")
        print("5. Count Words")
        print("6. Remove Extra Spaces")
        print("7. Reverse Text")
        print("8. Find if text is alpha numeric")
        print("9. Find if text is ends with")
        print("10. Center align")
        print("11. Count the occurance")
        print("12. Find index")
        print("13. Perform split")
        print("14. Perform partition")
        print("15. Perform Replace")
        print("16. Exit")

        choice = input("Enter your choice:")

        #uppercase
        if choice == "1":
            print(text_uppercase(text))
            break

        #lowercase choice
        elif choice == "2":
            print(text_lowercase(text))
            break

        #Capital case choice
        elif choice == "3":
            print(text_capitalcase(text))
            break

        #Count choice
        elif choice == "4":
            print(text_count(text))
            break

        #count words
        elif choice == "5":
            print(word_count(text))
            break

        #remove extra spaces
        elif choice == "6":
            print(remove_extra_spaces(text))
            break

        #reverse text
        elif choice == "7":
            print(reverse_text(text))
            break

        #is al num
        elif choice == "8":
            print(find_alphanum(text))
            break

        #text ends with
        elif choice == "9":
            word = input("Enter ending word:")
            print(text_endswith(text, word))
            break

        #center align
        elif choice == "10":
            width = int(input("Enter total width:"))
            print(center_align(text, width))
            break

        #Count the occurance
        elif choice == "11":
            word = input("Enter word or string to count occurance:")
            count = count_occurance(text, word)
            print(count)
            break

        #find index
        elif choice == "12":
            word = input("Enter word or string to find index:")
            print(find_index(text, word))
            break

        #perform split
        elif choice == "13":
            separator = input("Enter the separator:")
            print(perform_split(text, separator))
            break

        #perform partition
        elif choice == "14":
            partition = input("Enter partition")
            print(perform_partition(text, partition))
            break

        #perform replace
        elif choice == "15":
            oldval = input("Enter old val:")
            newval = input("Enter new val")
            print(perform_replace(text, oldval, newval))
            break

        elif choice == "16":
            print("Exiting program...")
            break

        else:
            print("Invalid choice, please try again")


text_manipulator()