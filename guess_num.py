# 讓使用者選擇隨機整數的範圍 (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "終於猜對了!"
# 猜錯的話 要告訴他 比答案大/小
# 一邊猜 一邊印出猜了幾次

import random
num_start = input('請決定隨機數字範圍開始值：')
num_start = int(num_start)
num_end = input('請決定隨機數字範圍結束值：')
num_end = int(num_end)
num = random.randint(num_start,num_end)
count = 0
while True:
	count += 1
	user_input = input(f'請從{num_start}到{num_end}猜1個數字:')
	user_input = int(user_input)
	if user_input == num:
		print('終於猜對了!')
		print('這是你猜的第', count, '次')
		break
	elif user_input > num:
		print('比答案大，再猜一次')
	elif user_input < num:
		print('比答案小，再猜一次')
	print('這是你猜的第', count, '次')