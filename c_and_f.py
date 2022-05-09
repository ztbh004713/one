c = input("請輸入目前的攝氏溫度: ")
c = float(c)
f = c * 1.8 + 32
print("目前的華氏溫度為: ", f ,"度。")

ff = input("請輸入目前的華氏溫度: ")
ff = float(ff)
cc = (ff - 32) * 5 / 9 
print("目前的攝氏溫度為:" , cc ,"度。")