alienDictionaly = {"こんにちは":"ガソパズッペ","私":"げっぺ","たち":"はべ","は":
"ふ","平和":"なべぼ","の":"ぎ","使者":"ぎひぎ","です":"なず","あなた":"どじむ","敵":
"はこ","で":"ま","ない":"ゆず","エネルギー":"ぱまほごぎゅ","と":"ち","食べ物":"むやさがゆ",
"を":"ち","分けて":"ぎもし","ください":"ぶぴねび"}
japanesephrase = input("エイリアン語にしたい文章を、一語ごとに半角スペースで区切って入力してください:") 
japanesewords = japanesephrase.split()
alienwords = []
for word in japanesewords:
    if word in alienDictionaly:
        alienwords.append(alienDictionaly[word])
    else:
        alienwords.append(word)
print("エイリアンはこういっています","".join(alienwords))
