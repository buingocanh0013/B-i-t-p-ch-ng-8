# Cho giá trị vả = 10, in ra màn hình các số chẳn lớn hơn 5 và <=10
# Sau đó in ra màn hình thông báo " Kết thúc lặp"
var = 10
while var > 0:
    if var %2 == 0:
        print("Giá trị :", var)
    var -=1
    if var ==5:
        break
print( "Kết thúc vòng lặp !!!")
