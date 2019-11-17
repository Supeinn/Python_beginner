import random
print("あなたは神秘的なお城の暗い部屋にいる")
print("目の前には4つのドアがある。君はどれか一つを選ばなければならない")
player_choise = input("1から4の数字を入力してください...")
if player_choise == "1" :
    print("宝もので一杯の部屋を見つけた。君は大金持ちだ!")
    print("君の勝ちだ!おめでとう")
elif player_choise == "2" :
    print("ドアを開くと怒り狂った人食い鬼が殴りかかってきた。")
    print("ゲームオーバー。君の負けだ。")
elif player_choise == "3":
    print("部屋に入ると龍が眠っているのを見つけた。")
    print("どうする？")
    print("1: 龍の宝を盗む")
    print("2: 見つからないようにこっそり出口へ向かう")
    dragon_choise = input("1か2を選んでください。")
    if dragon_choise == "1" :
        print("龍が目を覚ました。君は食べられてしまった...。美味しかったらしい...。")
        print("ゲームオーバー。君の負けだ。")
    elif dragon_choise == "2":
         print("君は龍のそばを通ってこっそりと城から抜け出せた。太陽の光が眩しい。")
         print("おめでとう。君の勝ちだ。")
    else :
        print("ごめんね。1か２を選んでね。")
elif player_choise == "4" :
    print("君はスフィンクスの部屋に入った。")
    print("スフィンクスが聞いてきた。『私が考えてる数を当ててみろ。1から10までのどれかだ。』")
    number = int(input("数字を選んでください・・・"))
    if number == random.randint(1,10):
        print("スフィンクスは、残念そうになった。『正解だ・・・』")
        print("スフィンクスは、君を解放した。自由だ。")
        print("おめでとう。君の勝ちだ。")
    else :
        print("スフィンクスは、違うと言った。")
        print("君は永遠に囚われの身となった。")
        print("ゲームオーバー君の負けだ。")
    
    
else:
    print("ごめんね。1から4のどれかを選んでね。")

print("やり直して別のドアに入ってみよう。")
