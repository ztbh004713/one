#读取档案+split()
#split()函式： 切割
#用前面撰写过的程式码来使用
products = [] 
with open("garbled.csv" , "r" , encoding="utf-8") as f: #因在原本写入时，已有撰写编码utf-8，因此再次读取档案时，也需要使用此编码来读取档案 
	for line in f:
		s = line.strip().split(",")                     #在split()函式中，添加字串逗号用以切割，split(",")
		print(s)									    #因在读取时会有换行的符号，需要撰写strip()来去除 \n（重点程式码由左至右依序执行）
											            #执行顺序line(str)>>  strip()  >>>  split(",") 
														#split 切割完的结果是清单(list)
#变数命名可因读取档案的数量来进行撰写，因档案中有四个栏位，其变数命名时，需撰写四个变数
#name, price, sugar, capacity = line.strip().split(",")                        
#products.append([name , price , sugar , capacity])     #在将读取出来的资料装进清单中，.append()



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

for p in products:
    print(p[0] , "的价格是：" , p[1] , "元 ," , "糖分：" , "," , p[2] , "商品的容量为：" , p[3] , "。")

with open("garbled.csv" , "w" , encoding="utf-8") as f:              
	f.write("商品,价格,糖分,容量\n")           
	for p in products:                           
		f.write(p[0] + "," + str(p[1]) + "," + p[2] + "," + p[3] + "\n")