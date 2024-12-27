# 1. Write a Python program to count the occurrences of each word in a given sentence.
#  string = “To change the overall look of your document.To change the look available in the gallery” 

def count_word_occurrences(sentence):

    words = sentence.split()

    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1

        else:
            word_counts[word] = 1

    return word_counts


sentences = input("Enter a Sentence : ")
print(count_word_occurrences(sentences))
