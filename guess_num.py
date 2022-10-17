# 產生一個隨機整數1~100 (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "終於猜對了!"
# 猜錯的話 要告訴他 比答案大/小

import random
num = random.randint(1,100)
while True:
	user_input = input('請從1到100，猜1個整數:')
	user_input = int(user_input)
	if user_input == num:
		print('終於猜對了!')
		break
	elif user_input > num:
		print('比答案大，再猜一次')
	elif user_input < num:
		print('比答案小，再猜一次')