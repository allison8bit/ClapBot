def clapify(sentence):
    sentence = sentence.upper()
    sentence = sentence.replace(" ", " :clap: ")
    return ":clap: " + sentence + " :clap:"
