woman = ["石原さとみ","ブル中野","マーガレット・サッチャー","橋本環奈"]
man = ["ケン・ヤスダ","安田顕","シルベスタ・スタローン","ノエル・ギャラガー"]
place = ["ハッテン場で","映画で","ファイトクラブで","エリア51で"]
shewore = ["パワーアーマー","マッスルスーツ","ハイレグ"]
hewore = ["変態水着","海パン","鎖かたびら"]
womansyas = ["犬の餌にシテヤル","始めようか","尊王攘夷"]
mansays = ["ハイ、イラッシャイ","任せときなサイドチェスト","御用改めである"]
consequense = ["後に伝説となった","世界は核の炎に包まれた","夢だった"]
worldsaid = ["'テンパイ'","'ユーアヒューマンだ'","'明日頑張ればいいじゃないか'"]
import random
while True :
   print(random.choice(woman),"は",random.choice(man),"に",random.choice(place),"で会った。")
   print("彼女は",random.choice(shewore),"を着ていた。")
   print("彼は",random.choice(hewore),"を着ていた。")
   print("彼女はこう言った。",random.choice(womansyas))
   print("そして彼はこう言った。",random.choice(mansays))
   print("その結果",random.choice(consequense))
   print("世界はこういった。",random.choice(worldsaid))
   print()
   input("もう一度遊ぶにはEnterキーを押してください。")
   print()
   
