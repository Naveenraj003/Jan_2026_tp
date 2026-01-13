def first_non_repeating_char(s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s:
        if freq[ch] == 1:
            return ch

    return None


if __name__ == "__main__":
    s = input("Enter string: ")
    result = first_non_repeating_char(s)

    if result:
        print("First non-repeating character:", result)
    else:
        print("No non-repeating character found")
