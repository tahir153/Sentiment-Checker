from textblob import TextBlob

x = input("Enter the sentence: ")
sentence_checked = TextBlob(x)
y = sentence_checked.sentiment.polarity
if y < 0:
    print("Negative")
elif y == 0:
    print("Neutral")
elif 0 < y <= 1:
    print("Positive")