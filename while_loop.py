pwd = input("请注册您的帐号： ")
num = input("请注册您的密码： ")
n = 5
f = 3
while True:
	n = n - 1
	pw = input("请输入您注册的帐号： ")
	if pwd == pw:
		print("输入正确。")
		break
	else:
		print("您还可输入的" , n ,"次数。")
		if n == 0:
			print("输入错误。")
			print("次数使用完，请再重新注册。")
			break
while True:
	f = f - 1
	nu = input("请输入您注册的密码： ")
	if num == nu:
		print("输入正确。")
		break
	elif num != nu:
		print("输入错误。")
		print("您还可输入的"  , f ,"次数。")
	elif f == 0:
		print("次数使用完，请再重新注册。")
		break
if pwd == pw and num == nu:
	print("进入游戏中 请稍后。")
	print("载入资源中")
	print("载入100%")
	print("成功登入")