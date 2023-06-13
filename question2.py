def is_palindrome_with_trash_symbols(InputString, TrashSymbolsString):
    # Convert InputString and TrashSymbolsString to lowercase
    input_string = InputString.lower()
    trash_symbols = TrashSymbolsString.lower()

    # Initialize pointers for the start and end of the string
    start = 0
    end = len(input_string) - 1

    # Traverse the string from both ends
    while start < end:
        # Ignore trash symbols in the comparison
        while input_string[start] in trash_symbols:
            start += 1
        while input_string[end] in trash_symbols:
            end -= 1

        # Compare the characters (ignoring case)
        if input_string[start] != input_string[end]:
            return False

        # Move the pointers
        start += 1
        end -= 1

    # If the traversal completes without any mismatches, it is a palindrome
    return True