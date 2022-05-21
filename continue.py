#continue教学
#读取档案跳过栏位名称
#在for回圈中使用
#continue跟break一样只能写在回圈里
#continue：跳到下一回的意思，并不会终止回圈

products = [] 
with open("garbled.csv" , "r" , encoding="utf-8") as f:  
	for line in f:
		if "商品,价格,糖分,容量" in line:							#if判断，并撰写条件确认
			continue 											#有继续的意思，在执行for回圈时，如果有碰到撰写的条件时，则后续程式码不执行，直接跳到下一回圈
		name, price, sugar, capacity = line.strip().split(",")                     
		products.append([name , price , sugar , capacity])
print(products)									   
