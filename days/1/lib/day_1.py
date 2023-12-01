
def parse_single_line(line):
    digit_characters = [c for c in line if c.isdigit()]
    return (10 * int(digit_characters[0])) + int(digit_characters[-1])

def parse_document(document):
    return sum(parse_single_line(line) for line in document.split("\n"))
