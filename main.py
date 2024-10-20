def count_words(text):
    words = text.split()
    return len(words)

def book_string(text):
    character_count = book_string(text.lower())
    print(character_count)


"""
These are my thoughts about what needs to happen based off of the count characters project requirements:
    - convert book into string
    - a dictionary with [characters, integers]
    - convert characters to lowercase 
    - Im going to need to have a running total for characters as integers
    - i need to update the character dictionary to only add new letters not repeat each letter
    
"""
    


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    #print(file_contents)

    word_count= count_words(file_contents)
    print(f"Word count: {word_count}")


if __name__ == "__main__":
    main()
