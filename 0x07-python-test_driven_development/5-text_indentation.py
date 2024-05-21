#!/usr/bin/python3
def text_indentation(text):
    new_text = ""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        new_text += text[i]
        if text[i] in [".", ":", "?"]:
            new_text += "\n\n"
            if i + 1 < len(text) and text[i + 1] == " ":
                i += 1
        i += 1
    new_text += "\n"
    print(new_text, end="")
