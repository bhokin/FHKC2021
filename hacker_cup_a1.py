t = int(input())
word_list = []

for _ in range(t):
    s = input()
    word_list.append(s)

for _ in range(t):
    if len(word_list[_]) == 1:
        print(f"Case #{_ + 1}: 0")
    else:
        letter = 26 * [0]
        vowel, consonant, max_vowel, max_consonant = 0, 0, 0, 0

        for i in word_list[_]:
            letter[ord(i) - 65] += 1  # เพิ่มจำนวนของตัวอักษร
            if i == 'A' or i == 'E' or i == 'O' or i == 'U' or i == 'I':
                vowel += 1
                if letter[ord(i) - 65] > max_vowel:
                    max_vowel = letter[ord(i) - 65]
            else:
                consonant += 1
                if letter[ord(i) - 65] > max_consonant:
                    max_consonant = letter[ord(i) - 65]

        if vowel <= consonant:
            print(f"Case #{_ + 1}: {consonant + 2 * (vowel - max_vowel)}")
        else:
            print(f"Case #{_ + 1}: {vowel + 2 * (consonant - max_consonant)}")
