def count_words(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

sentence = "I love Python programming. Python is fun!"
word_counts = count_words(sentence)
for word, count in word_counts.items():
    print(word + ":", count)