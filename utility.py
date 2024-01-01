def txt_to_list(path):
    file = open(path)
    words = []
    for line in file:
        words.append(line.strip())

    file.close()
    return words
