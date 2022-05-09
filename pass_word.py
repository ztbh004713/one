password = "a123456"
x = 3
while x > 0:
	pas = input("請輸入密碼: ")
	x = x - 1
	if pas == password:
		print("恭喜輸入正確。")
		break
	else:
		print("密碼輸入錯誤!" , "還有" , x ,"次機會。")
		if x == 0:
			print("帳號已被鎖定，請聯繫客服!!")
