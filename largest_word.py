def largest_word(sentence):
    words = sentence.split()  # Split the sentence into words
    if not words:
        return None  # Return None if the sentence is empty

    largest = ''
    for word in words:
        if len(word) > len(largest):
            largest = word  # Update the largest word if a longer word is found

    return largest

# Test case
input_sentence = "This is a test sentence to find the largest word yrdsrxfyksrxf"
result = largest_word(input_sentence)
print("The largest word is:", result)