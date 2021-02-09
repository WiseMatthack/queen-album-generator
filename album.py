import markovify

# Get raw text as string.
with open("D:/matth/Documents/queengendeluxe/album.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.NewlineText(text)

# Print five randomly-generated sentences
for i in range(35):
    print(text_model.make_sentence(tries=1000))