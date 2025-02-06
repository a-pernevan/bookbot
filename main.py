
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    # print(file_contents)
    # print(count(file_contents))
    report(letters(file_contents))

def count(file_contents):
    words = file_contents.split()
    return len(words)

def letters(file_contents):
    file_contents = file_contents.lower()
    letter_count = {}
    
    for letter in file_contents:
        if letter in letter_count:
            letter_count[letter] = int(letter_count[letter]) + 1

        else:
            letter_count[letter] = 1

    return letter_count

def report(letter_count):
    for letter, count in letter_count.items():
        if letter.isalpha():
            print(f"The '{letter}' character was found {count} times")

main()