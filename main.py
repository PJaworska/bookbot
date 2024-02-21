def main():
    print("--- Begin report of frankenstein.txt ---")
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    words_count = len(words)
    print(f"{words_count} words found in the document \n")
    letter_count(words)
    


def letter_count(words):
    alphabet_count = {}
    for word in words:
        for letter in word.lower():
            if not letter.isalpha():
                continue
            if letter not in alphabet_count:
                alphabet_count[letter] = 0
            alphabet_count[letter] +=1

    letter_count_list = []
    for key, lcount in alphabet_count.items():
        letter = {
            "letter": key,
            "how_many": lcount,
        }
        letter_count_list.append(letter)

    letter_count_list.sort(reverse=True, key=how_many_key)

    for element in letter_count_list:
        print(f"The '{element["letter"]}' was found {element["how_many"]}")
    return letter_count_list


def how_many_key(dct):
    return dct["how_many"], dct['letter']
    





main()
