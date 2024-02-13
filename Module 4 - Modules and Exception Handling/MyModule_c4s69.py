def func1(name):
     print(f"Hi,{name} welcome to my module")

def func2(lst):
    even=[]
    odd=[]
    for i in lst:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    print(f"Even:{even},odd:{odd}")

