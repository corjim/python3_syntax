# Turn that into a function, print_upper_words. Test it out. (Don’t forget to add a docstring to your function!)

def print_upper_words(words):
    """Each letter/word is printed on seperate line, uppercased.

        print_upper_words(['kangaroo', 'blonde', 'babies'])
        KANGAROO
        BLONDE
        BABIES
    """

    for word in words:
        print(word.upper())

# Turn that into a function, print_upper_words. Test it out. (Don’t forget to add a docstring to your function!)

def print_upper_words_with_e_or_E(words):
    """ If starts with E or e, words will print uppercased in a seperate line.

        print_upper_words_with_e_or_E(["event", "advantage", "ALLUR"])
        EVENT
        ADVANTAGE
    """

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


# Make your function more general: you should be able to pass in a set of letters, and it only prints words that start with one of those letters.

def print_upper_words3(words, must_start_with):
    """Print each word on sep line, uppercased, if starts with one of given

        >>> print_upper_words3(["eagle", "Edward", "Alfred", "zope"],
        ...                   must_start_with=["A", "E"])
        EDWARD
        ALFRED
    """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break
