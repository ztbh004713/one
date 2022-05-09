import random
gus = random.randint(1, 150)
g = 0
while True:
	g = g + 1
	sub =input("請猜一個數字: ")
	sub = int(sub)
	if gus == sub:
		print("恭喜您猜對了。")
		break
	elif sub < gus:
		print("猜得太低了，再往高一點猜.")
		print("這是您猜的第 ", g , "次")
	elif sub > gus:
		print("猜得太高了，再往低一點猜.")
		print("這是您猜的第 ", g , "次")
	if g >= 15:
		print("猜这么多次，还没猜中真可惜")
		print("下次在努力。")
		break