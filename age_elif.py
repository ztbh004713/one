country = input("請輸入您的國家: ")
age = input("請輸入您的年齡: ")
age = int(age)
if country == "tw":
	if age >= 18:
		print("您的國籍為TW，年紀符合考照。")
	elif age < 18:
		print("因年齡不符合，無法考照。")
elif country == "us":
	if age >= 16:
		print("您的國籍為US，年紀符合考照。")	
	elif age < 16:
		print("因年齡不符合，無法考照。")		
else:
	print("輸入的國家不符合，請再重新輸入。")
