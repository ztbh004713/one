age = input("請輸入您的年齡: ")
age = int(age)
if age >= 18 and age <20:
	print("刑法已成年")
elif age >=20:
	print("民法已成年")
elif age >= 30 and age < 55:
	print("正值青壯年")