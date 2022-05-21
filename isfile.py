#检查档案在不在
#import os (作业系统模组：operating system)
import os

products = [] 	#将清单建立在最开始撰写程式的时候，用意是不管程式是否有找到档案而执行时需要用到，或是后续给予使用者输入时也会用到，撰写在最开始从而避免程式出错	
if os.path.isfile("garbled.csv"):        #检查档案、读取档案			
	print("已有确认此档案")
	with open("garbled.csv" , "r" , encoding="utf-8") as f:  
		for line in f:
			if "商品,价格,糖分,容量" in line:							
				continue 											
			name, price, sugar, capacity = line.strip().split(",")                     
			products.append([name , price , sugar , capacity])
	print(products)							
else:
	print("找不到此档案。")

#给予使用者输入新商品
while True:                              
    name = input("請輸入商品名稱: ")        
    if name == "exit":                     
        break                               
    price = input("請輸入商品價格: ") 
    price = int(price)                           
    sugar = input("请输入商品糖分: ")
    capacity = input("请输入商品容量: ")       
    products.append([name , price , sugar , capacity])                       
print(products) 

#印出所有购买记录
for p in products:
    print(p[0] , "的价格是：" , p[1] , "元 ," , "糖分：" , "," , p[2] , "商品的容量为：" , p[3] , "。")

#写入档案
with open("write.csv" , "w") as f:               
	for p in products:                           
		f.write(p[0] + "," + str(p[1]) + "," + p[2] + "," + p[3] + "\n") 