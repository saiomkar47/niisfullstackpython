#swaping with using third variable
a=10
b=20
print("before swaping a=",a,"b=",b)
t=a
a=b
b=t
print("after swaping a=",a,"b",b)



#with out using third variable 
a=3
b=5
print("before swaping a=",a,"b=",b)
a=a+b
b=a-b
a=a-b
print("before swaping b=",b,"a=",a)



a=10
b=20
a,b=b,a
print(a,b)


#swaping three no left to right with 4th variable
a=4
b=7
c=5
t=c
c=b
b=a 
a=t
print(a,b,c)