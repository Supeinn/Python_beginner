import random
number = random.randint(1,20)
guess = int(input("1から20の整数を考えているよ。当ててみて。"))
while guess != number: 
    if guess < number:
         print("それじゃ小さいよ。")
    else:
        print("それじゃ大きいよ。")
    guess = int(input("今度こそ当ててみて"))
print("おめでとう!正解だよ！")
            
            
