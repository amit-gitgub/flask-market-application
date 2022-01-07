

def countwordoccuerence(string, word):
    count = 0
    for i in string.split():
        if i.lower() == word:
            count = count + 1

    return count


def countcharacterOccurence(string, character):
    count = 0
    for i in string:
        if i == character:
            count = count + 1

    return count

charactercount = countcharacterOccurence("this is my name and i am aaaa good boy", 'a')
wordcount = countwordoccuerence("To count the occurrences of a character, we need to write an algorithm that returns the number of times each character appears in the input string. The algorithm must iterate through each character from the beginning to count the number of times each character appears in the string. Here’s how to write an algorithm for counting character occurrences using Python","to")

print(charactercount)
print(f"to appeared {wordcount} times")
