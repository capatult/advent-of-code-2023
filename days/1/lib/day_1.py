DIGIT_WORDS = (
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
)
DIGIT_WORD_DECODER = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

def parse_single_line(line):
    digit_characters = [c for c in line if c.isdigit()]
    return (10 * int(digit_characters[0])) + int(digit_characters[-1])

def parse_document(document):
    return sum(
        parse_single_line(line) 
        for line in document.split("\n")
    )

def parse_single_line_with_words(line):
    digits = []
    for i, c in enumerate(line):
        if c.isdigit():
            digits.append(int(c))
        for digit_word in DIGIT_WORDS:
            if line[:i + 1].endswith(digit_word):
                digits.append(DIGIT_WORD_DECODER[digit_word])
    return (10 * digits[0]) + digits[-1]

def parse_document_with_words(document):
    return sum(
        parse_single_line_with_words(line)
        for line in document.split("\n")
    )

# if __name__ == "__main__":
#     with open("../puzzle_input.txt") as puzzle_input:
#         print(parse_document(puzzle_input.read()))

if __name__ == "__main__":
    with open("../puzzle_input.txt") as puzzle_input:
        print(parse_document_with_words(puzzle_input.read()))
