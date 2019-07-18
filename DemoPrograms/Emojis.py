def emoji_convertor(message):
    words = message.split()

    emojis = {
        ":)": "\U0001F609",
        ":(": "\U0001F614",
        "::": "\U0001F60E"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


print(emoji_convertor(input('>')))
