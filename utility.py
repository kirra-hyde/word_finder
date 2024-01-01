
def txt_to_list(path):
    file = open(path)
    return [line.strip() for line in file if (line.strip() and line[0] != "#")]
