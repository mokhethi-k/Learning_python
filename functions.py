def emoji_conv(message):
    words = message.split(" ")
    emojis = {
        ":)": "😊😊😊😊",
        ":(": "😠😠😠😠",
    }
    output = ""
    for word in words:
        output += emojis.get(word, word + " ")
    return output


em = input(">> Type your message: ")
print(emoji_conv(em))


