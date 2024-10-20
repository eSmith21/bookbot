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

    word_count = count_words(file_contents)
    char_count_dict = count_characters(file_contents)

    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    char_list = []
    for char, count in char_count_dict.items():
        char_list.append({"char": char, "num": count})

    char_list.sort(key=lambda x: x["num"], reverse=True)

    for char_dict in char_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")

    print(f"--- End report ---")

#char_count = count_characters(file_contents)
    #sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    main()
