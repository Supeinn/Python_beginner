alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
stringToEncrypt = input("暗号化するメッセージを、ローマ字で入力してください:")
stringToEncrypt =stringToEncrypt.upper()
shiftAmount = int(input("1から25のどれかの数を指定してください:"))
encryptedstring = ""
for currentCharacter in stringToEncrypt:
    position = alphabet.find(currentCharacter)
    newposition = position + shiftAmount
    if currentCharacter in alphabet:
        encryptedstring = encryptedstring + alphabet[newposition]
    else:
        encryptedstring = encryptedstring + currentCharacter
print("暗号化したメッセージ:",encryptedstring)
