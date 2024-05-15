def is_pangram(st):
    sentence = st.lower()

    unique_letters = set()

    for char in sentence:
        if 'a' <= char <= 'z':
            unique_letters.add(char)
    return len(unique_letters) == 26

if __name__ == "__main__":
    print(is_pangram("The quick brown fox jumps over the lazy dog"))