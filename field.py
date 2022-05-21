#栏位的添加
products = []                                   #
while True:                              
    name = input("請輸入商品名稱: ")        
    if name == "exit":                     
        break                               
    price = input("請輸入商品價格: ") 
    price = int(price)                           #再输入价格的时候，可将其型态转换为整数
    sugar = input("请输入商品糖分: ")
    capacity = input("请输入商品容量: ")       
    products.append([name , price , sugar , capacity])                       
print(products) 

for p in products:
    print(p[0] , "的价格是：" , p[1] , "元 ," , "糖分：" , "," , p[2] , "商品的容量为：" , p[3] , "。")

#在档案中添加栏位
#撰写程式码来写入栏位资讯
#在写入档案的程式当中添加一段程式码
with open("field.csv" , "w") as f:               
	f.write("商品,价格,糖分,容量\n")           #需在for回圈前，就先撰写此段程式码避免重复写入 （\n 换行）
	for p in products:                           
		f.write(p[0] + "," + str(p[1]) + "," + p[2] + "," + p[3] + "\n") 


