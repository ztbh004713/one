#解决乱码问题
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


#写入档案中的栏位显示乱码
#解决乱码问题（编码encoding）
#utf-8 几乎为世界通用(可用来读各种符号，语言)
#在撰写with open的程式码当中，撰写：encoding="utf-8"
with open("garbled.csv" , "w" , encoding="utf-8") as f:       #open(档名+模式+语言编码)        
	f.write("商品,价格,糖分,容量\n")           
	for p in products:                           
		f.write(p[0] + "," + str(p[1]) + "," + p[2] + "," + p[3] + "\n") 