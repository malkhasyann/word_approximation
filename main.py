"""
    Suggests similar words for the given word.
    Using Levenshtein distance to measure the distance between two strings.
"""


def lev(word1, word2):
    """ Levenshtein distance """
    table = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]

    for i in range(len(table[0])):
        table[0][i] = i

    for i in range(len(table)):
        table[i][0] = i

    for row in range(1, len(table)):
        for col in range(1, len(table[0])):
            if word1[col - 1] == word2[row - 1]:
                table[row][col] = table[row - 1][col - 1]
            else:
                table[row][col] = 1 + min([table[row - 1][col - 1], table[row][col - 1], table[row - 1][col]])

    return table[-1][-1]


if __name__ == '__main__':
    # take the words from the file and cut newline characters
    with open('words.txt', 'r', encoding='utf-8') as file:
        words = [word.strip() for word in file.readlines()]

    given_word = input('Enter your word: ')  # take a word from user
    answers = []  # container for similar words
    for word in words:
        # if matched break the loop
        if lev(given_word, word) == 0:
            print('There is such a word in the list!')
            break
        # add the similar word
        if lev(given_word, word) <= 2:
            answers.append(word)
    else:
        # if the loop was not broken
        # print suggestions
        if answers:
            print('Did you mean')
            for word in answers:
                print(f'\t{word}')
        else:
            print('Sorry, there is no suggestions for this word.')
