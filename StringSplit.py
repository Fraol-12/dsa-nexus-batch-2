def split_and_join(line):
    # Split the line into words based on spaces
    words = line.split(" ")
    # Join the words with hyphens
    return "-".join(words)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
