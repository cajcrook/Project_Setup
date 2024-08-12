def get_most_common_letter(text):
    # print(" * Text:")
    # print(text)
    counter = {}
    text = text.replace(" ","")
    text = text.replace("!","")
    text = text.replace(",","")
    print(" * print updated text")
    print(text)
    for char in text:
        # print(" * char:")
        # print(f'Line 7 {char}')
        counter[char] = counter.get(char, 0) + 1
        # print (counter[char])
        # print(counter.get(char,0)+1)
    letter = sorted(counter.items(), key=lambda item: item[1])[-1][0]
    # print(sorted(counter.items(), key=lambda item: item[1]))
    # print(counter)
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")

