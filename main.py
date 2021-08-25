""" Tate Stradling
    08/13/2021
    Tavin Translator """

import re
import math

keys = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
        "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1",
        "2", "3", "4", "5", "6", "7", "8", "9")
values = ("ai", "ou", "ie", "ia", "aa", "iu", "oe", "eo", "au", "uo", "ue",
          "eu", "io", "ea", "ao", "oa", "uu", "ei", "ee", "ae", "ii", "ua",
          "oi", "ui", "oo", "yy", "ya", "ay", "oy", "yu", "yi", "iy", "yo",
          "ye", "ey", "uy")


def encrypt(word_e):
    """ Encrypts single words to Tavin. """

    translated_word = ""

    # For every character in word_e, translate and add to translated_word
    for char in word_e:
        translated_word += values[keys.index(char)]
    # Returns output
    return translated_word


def decrypt(word_d):
    """ Decrypts single words from Tavin. """

    translated_word = ""

    # For every 2 characters in word_d, translate and add to translated_word
    for char_index in range(0, len(word_d), 2):
        translated_word += keys[values.index(word_d[char_index] +
                                             word_d[char_index + 1])]
    # Returns output
    return translated_word


def word_index_separator(input_str_ws):
    """ Separates input string into multiple words,
        and returns index values. """

    word_index_list = []

    """ Loops over matches for words in input string, and saves index values to
        array. """
    for match_ws in re.finditer(r'\b\w+(?:[@\'.]\w|\w)*', input_str_ws):
        temp_word_index_tuple = (match_ws.start(), match_ws.end() - 1)
        word_index_list.append(temp_word_index_tuple)

    # Returns the word index list, converted to a tuple
    return tuple(word_index_list)


def tavin_translator_core(input_str_tt, to_or_from_tavin_tt,
                          double_translate_tt, loops_tt):
    """ Takes input string, boolean 'to or from tavin', whether or
        not to double encrypt, and how many times to recursively call the
        function through the loop_tt variable. Then evaluates if the input can
        be properly translated, breaks it up so it can be translated,
        translates it with the decrypt and encrypt functions. It then puts the
        separate words back together with the corresponding punctuation and
        recursively calls the function if needed (loop_tt var). When finished,
        it returns translated input. """

    """ Checks if translator is decrypting, not double decrypting, and if
        input string contains non-vowels or numbers. If the input string
        contains non-vowels or numbers, returns invalid input. """
    if not to_or_from_tavin_tt and not double_translate_tt:
        non_vowels_and_numbers_match = re.search('[b-df-hj-np-tv-xz0-9]',
                                                 input_str_tt.lower())

        # Returns that input is invalid
        if non_vowels_and_numbers_match:
            return False, ""

    # Separates input string into multiple words, and returns index values
    word_index_tuple = word_index_separator(input_str_tt)

    # String where translated sentence is compiled
    translated_input = ""

    # Counts each loop of word_index_tuple for loop
    word_index_counter = 0

    """ Loops over each word in input sentence using the word_index_tuple
        returned by the word_index_separator function, and marks the indexes of
        special characters contained in words like apostrophes, at symbols,
        and periods contained in email addresses. It also marks the indexes
        of capitalized letters in a list. Then, it creates a temporary word
        without the special characters, and with converted capitalized-to-
        -lower-case letters in preparation for the translation. It then
        translates each simplified word with the appropriate decrypt or
        encrypt function. It then combines translated word with proper
        punctuation and capitalization to return the proper translation
        output. """
    for word_index in word_index_tuple:

        # Temporary word to pass as argument to decrypt or encrypt function
        temp_word_no_special_chars = ""

        # Finished translated word, ready to be combined into sentence.
        translated_word = ""

        """ List of indexes of special characters, as special characters
            aren't added to the temporary word. """
        special_char_index_list = []

        """ List of indexes of capitalized letters, as capitalized letters
        are converted to lower case for temporary word. """
        capitalized_index_list = []

        # Loops over each character in the word currently being translated.
        for char_index in range(word_index[0], word_index[1] + 1):

            """ Adds any special characters in the word to the special
                character index list, and don't add the special character
                to the temporary word, because it can't be translated. """
            if re.search(r'[^a-zA-Z0-9]', input_str_tt[char_index]):
                special_char_index_list.append(char_index)

            # Detailed description of statement within elif statement
            elif re.search(r'[A-Z]', input_str_tt[char_index]):
                """ Adds any capitalized letters to the capitalized letter
                    index. Then adds the lowercase version of each capitalized
                    letter to the temp word so it can be translated, and then
                    capitalized letters can be added back after translation
                    using the capitalized letter index. """
                capitalized_index_list.append(char_index)
                temp_word_no_special_chars += \
                    input_str_tt[char_index].lower()

            # If the character is a lower-case letter/number add to temp word
            else:
                temp_word_no_special_chars += input_str_tt[char_index]

        # If single decrypting
        if not to_or_from_tavin_tt and not double_translate_tt:

            """ If any word has an odd amount of characters, return False
            in the 0th index location of the return tuple to signify that the
            input is invalid. """
            if len(temp_word_no_special_chars) % 2 != 0:
                return False, output

        # If double translating, proceed to translate
        if double_translate_tt:
            encrypted_word = encrypt(temp_word_no_special_chars)

            """ Double encrypts to tavin, saves to
                translated_word var. """
            if to_or_from_tavin_tt and double_translate_tt:

                """ Decrypts encrypted_word var with the first character in
                    string moved to the back (double encrypting). """
                translated_word = decrypt(
                    encrypted_word[1:] + encrypted_word[0])

            # Double decrypts to tavin, saves to
            # translated_word var
            elif not to_or_from_tavin_tt and double_translate_tt:
                end_char_index = len(encrypted_word) - 1

                """ Decrypts encrypted_word var with the last character in
                    string moved to the back (double decrypting). """
                translated_word = \
                    decrypt(encrypted_word[end_char_index] +
                            encrypted_word[:end_char_index])

        # Encrypts to tavin, saves to translated_word var
        elif to_or_from_tavin_tt:
            translated_word = \
                encrypt(temp_word_no_special_chars)

        # Decrypts to tavin, saves to translated_word var
        else:
            translated_word = \
                decrypt(temp_word_no_special_chars)

        """ Replaces each special character into corresponding index in
            translated word. """
        for special_char_index in special_char_index_list:
            """ If double translating, add special character in same index as
                before. """
            if double_translate_tt:

                # Finds which index in word should be added
                char_index_relative_to_word = \
                    special_char_index - word_index[0]

                # Adds appropriate index in translated word
                translated_word = \
                    translated_word[:char_index_relative_to_word] + \
                    input_str_tt[special_char_index] + \
                    translated_word[char_index_relative_to_word:]

            # More comments available in elif statement
            elif to_or_from_tavin_tt:
                """ If single encrypting, add special character in the
                    index * 2 of before, due to the nature of Tavin. """

                # Finds which index in word should be added
                char_index_relative_to_word = \
                    (special_char_index - word_index[0]) * 2

                # Adds appropriate index in translated word
                translated_word = \
                    translated_word[:char_index_relative_to_word] + \
                    input_str_tt[special_char_index] + \
                    translated_word[char_index_relative_to_word:]
                print(translated_word)

            # More comments available in else statement
            else:
                """ If single encrypting, add special character in the
                    index / 2 (rounded up) of before, due to the nature of
                    Tavin. """

                # Finds which index in word should be added
                char_index_relative_to_word = \
                    math.ceil((special_char_index - word_index[0]) / 2)

                translated_word = \
                    translated_word[:char_index_relative_to_word] + \
                    input_str_tt[special_char_index] + \
                    translated_word[char_index_relative_to_word:]

        """ Capitalizes each corresponding capitalized index in translated word
            as is capitalized in input string. """
        for capitalized_index in capitalized_index_list:

            # If double translating, capitalize same index as before
            if double_translate_tt:

                # Finds which index in word should be capitalized
                cap_index_relative_to_word = capitalized_index - word_index[0]

                # Capitalizes appropriate index in translated word
                translated_word = \
                    translated_word[:cap_index_relative_to_word] + \
                    translated_word[cap_index_relative_to_word].upper() + \
                    translated_word[cap_index_relative_to_word + 1:]

            # More comments available in elif statement
            elif to_or_from_tavin_tt:
                """ If single encrypting, capitalize the character of
                    index * 2 of before, due to the nature of Tavin. """

                # Finds which index in word should be capitalized
                cap_index_relative_to_word = \
                    (capitalized_index - word_index[0]) * 2

                # Capitalizes appropriate index in translated word
                translated_word = \
                    translated_word[:cap_index_relative_to_word] + \
                    translated_word[cap_index_relative_to_word].upper() + \
                    translated_word[(cap_index_relative_to_word + 1):]

            # More comments available in else statement
            else:
                """ If single decrypting, capitalize the character of
                    index / 2 (rounded up) of before, due to the nature of
                    Tavin. """

                # Finds which index in word should be capitalized
                cap_index_relative_to_word = \
                    math.ceil((capitalized_index - word_index[0]) / 2)

                # Capitalizes appropriate index in translated word
                translated_word = \
                    translated_word[:cap_index_relative_to_word] + \
                    translated_word[cap_index_relative_to_word].upper() + \
                    translated_word[cap_index_relative_to_word + 1:]

        """ If this is the first word in the index, add all previous special
            characters to translated_input. """
        if word_index == word_index_tuple[0]:
            translated_input = input_str_tt[:word_index[0]]

        # Adds each translated word to translated input
        translated_input += translated_word

        """ If there is another word in the word index tuple, adds in the
            special characters between this word and the next word to the
            translated input. """
        if len(word_index_tuple) > word_index_counter + 1:
            translated_input += \
                input_str_tt[word_index[1] + 1:
                             word_index_tuple[word_index_counter + 1][0]]

        # If there isn't another word to translate, add in any following chars.
        else:
            translated_input += input_str_tt[word_index[1] + 1:]

        # Adds 1 to loop counter
        word_index_counter += 1

    """ If the user wants to loop over translator, recursively calls the
        function to loop over the input string, and returns output. """
    if loops_tt > 1:
        return tavin_translator_core(translated_input, to_or_from_tavin_tt,
                                     double_translate_tt, loops_tt - 1)

    # Outputs translated input to previous function
    return True, translated_input


if __name__ == "__main__":
    # Greet user
    print("Welcome to Tavin Translator!")

    """ Translate to Tavin from text, or to text from Tavin? Default value set
        to Tavin from text. """
    to_or_from_tavin = True

    # Loops over user input until valid input for to_or_from_tavin
    while True:
        to_or_from_tavin_input = input("Would you like to convert from text to"
                                       " Tavin, or Tavin to text? (1, 2) >")
        if to_or_from_tavin_input == "1":
            break

        elif to_or_from_tavin_input == "2":
            to_or_from_tavin = False
            break

        print("Please enter valid input.")

    """ Double encrypting is Tavin slang for encrypting to Tavin, moving the
        first vowel of each encrypted word to the end of each encrypted word,
        and decrypting the modified word. It decrypts into a seemingly random
        word of letters and numbers the same length of the original. """
    double_translate = False

    # Loops over user input until valid input for double_translate
    while True:
        double_translate_input = ""

        """ Depending on if user is encrypting or decrypting, ask the user if
            they want to double encrypt or decrypt. """
        if to_or_from_tavin:
            double_translate_input = input("Would you like to double "
                                           "encrypt? (Yes, No) >")
        else:
            double_translate_input = input("Would you like to double "
                                           "decrypt? (Yes, No) >")

        # If user input is yes or no, continue. Otherwise, loop over again.
        if double_translate_input.lower() in ["yes", "no"]:
            if double_translate_input.lower() == "yes":
                double_translate = True
            else:
                double_translate = False
            break

        print("Please enter valid input.")

    # How many times input is translated using tavin translator
    loops = 1

    """ Unless double_translate is activated, loop over user input
        until valid input for loops variable, or user inputs they don't want to
        translate multiple times. """
    while not double_translate:
        multipleLoops = input("Would you like to translate input multiple "
                              "times? (Yes, No) >")
        # If input isn't equal to "yes" or "no", input loop starts over
        if multipleLoops.lower() in ["yes", "no"]:

            """ If user wants to translate multiple times, program enters into
                second input loop """
            while multipleLoops.lower() == "yes":
                loopInput = input("How many times do you want to loop over? >")

                """ Raises value error exception if input can't convert to int,
                    or if input is less than 1. """
                try:
                    if int(loopInput) < 1:
                        raise ValueError()

                    loops = int(loopInput)

                except ValueError:
                    print("Please enter valid input.")
                    continue
                break
            break

        else:
            print("Please enter valid input.")

    # Translated input that will be outputted to user
    output = ""

    """ While there's no output, loop over input loop, getting input string
        from user, verify input is valid, and translate according to user
        specifications. Translate input to Tavin when valid user input is
        obtained. """
    while output == "":
        input_str = input("What do you want to translate? >")

        # Verifies user input is valid, and translates to Tavin
        tavin_translator_core_tuple = \
            tavin_translator_core(input_str, to_or_from_tavin,
                                  double_translate, loops)

        # If user input is invalid, returns to beginning of loop
        if not tavin_translator_core_tuple[0]:
            print("Please enter valid input.")
            continue

        output = tavin_translator_core_tuple[1]

    # Prints output
    print("Output: " + output)
