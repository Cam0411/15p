#cau 1 
n1 = int(input("nhap n1: "))
n2 = int(input("nhap n2: "))
d  = int(input("nhap d:  "))
t = range(n1,n2,d)

#cau 2 
print("Cau2:  in ra cac so:  ")
for i in t:
    print(i,end=" ")

#cau 3 
k = 0 
for i in t:
    k = k + i 
print("\nCau 3: tong cac so: ","\n",k)

#cau 4 
c = 0 
for i in t:
    if i % 3 == 0:
        c = c + 1 
print("Cau 4: tong cac so chi het cho 3 la: ","\n",c)

#cau 5 
a = int(input("nhap a: "))
if a in t:
    print("co gia tri a")
else:
    print("ko co gia tri a")