def group_anagrams(words):
    anagrams = {}

    for word in words:
        key = ''.join(sorted(word))
        anagrams.setdefault(key, []).append(word)

    return list(anagrams.values())


if __name__ == "__main__":
    words = input("Enter words: ").split()
    result = group_anagrams(words)

    for group in result:
        print(group)
