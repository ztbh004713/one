#parameter-参数篇
#parameter(参数)，形容成投币孔：
#1.当#function需要外部资料的时候，我们就设计投币孔(参数)，把资料投进去#function里面。
#(因为让#function读取程式码架构外部的资料是不佳的) 
#2.如果#function有投币孔，就一定要投东西(除非参数有预设值)。
#3.投东西的时候自动是按照参数的顺序。
#4.参数可以有"预设值"，那就不一定要投给它。
#5.投东西给参数的时候可以"明确指定"要投到哪一个参数。

def money(one):							#one：撰写的参数，上述重点有特别告知，参数要撰写在架构内，不应该撰写在架构外
	print("要领钱")
	print("缴卡费")
	print("买晚餐")
	if one:								#此处的 one 等同于 第10行的one
		print("买明天早餐")
money(True)								#括号中撰写True时，等于第十行的one为True，后续会进入if程式码当中
money(False)							#括号中撰写False时，等于第十行的one为False，因判断为错的，则不印出参数

def add(x , y):							#当撰写的参数有两个(含)以上，就需要给予相对应的值，否则程式会出现错误
	print(x + y)						#上述重点有特别说明的，设定的值，会按照参数的顺序印出
	print(x * y)
add(7 , 9)								#会先印出7+9在印出7*9，而后在执行下一个程序
add(40 , 90)		

#参数预设值
def odds(a=1 , b=1):            		#撰写参数时，等号左右不用空格（重点）
	print(a + b)
odds()									#当def撰写的参数有设定预设值，在使用此函式时，如没特别撰写，则会依照预设值执行
odds(5)									#当有预设值时，在使用函式，可只输入一个值，而这个值会给予第一个参数
odds(b=5)								#也可特别指定其中的值

def wash(dry=False , water=7 , end=0):	#设定三个参数
	print("加水" , water , "分满")		#这里的变数water会随著参数被输入不同的值而改变
	print("添加洗衣粉")
	print("调整模式")
	if dry:								#原先预设dry和end，也会因给予的参数设定不同而有所变动
		print("设定烘衣服")
	if end:
		print("晾衣服")
wash()
print("----------------")
wash(water=9 , end=False)
print("----------------")								
wash(dry=True , end=True)