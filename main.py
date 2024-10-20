def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = text.lower()
    char_count = {}
    for character in characters:
        if character.isalpha():
            if character in char_count:
                char_count[character] += 1
            else:
                char_count[character] = 1
    return char_count



def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    #print(file_contents)

    word_count= count_words(file_contents)
    print(f"Word count: {word_count}")

    char_count = count_characters(file_contents)
    sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    for char_count in sorted_chars:
        print(f"{char_count[0]}: {char_count[1]}")

if __name__ == "__main__":
    main()
