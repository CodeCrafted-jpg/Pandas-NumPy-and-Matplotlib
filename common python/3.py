marks={}

x=int(input("Enter marks for math: "))
marks.update({"maths":x})

y=int(input("Enter marks for physics: "))
marks.update({"physics":y})

print(marks)

# While loop
n=int(input("Enter a number: "))
i=1
while i <=10:
    print(n,"x",i,"=",n*i)
    i+=1
list=[1,4,9,16,25,36,49,64,81,100]
i=len(list)-1
j=0
while j<=i:
    print(list[j])
    j+=1

tuple=(1,4,16,25,36,49,64,81,100)

i=len(tuple)-1
j=0
while j<=i:
    print(tuple[j])
    j+=1

tuple=(1,4,16,25,36,49,64,81,100)
x=49
j=0
while j<=len(tuple)-1:
    if tuple[j]==x:
        print("Found at ", j,"th position")
        break
    j+=1

list=[1,4,9,16,25,36,49,64,81,100]

for i in list:
    print(i)

x=81

for i in list:
    if i==x:
        print("Found at ", list.index(i),"th position")
        break

n=int(input("Enter a number: "))
i=1
for j in range(i,n-1):
    print(i*j)
    i +=1