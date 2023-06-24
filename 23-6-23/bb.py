stu_gra=[]
stu_gra.append((1,"praneeth"))
stu_gra.append((2,"ajay"))
stu_gra.append((3,"nataraj"))
stu_gra.append((4,"ajay"))
stu_gra.sort(reverse=True)
print("yes")
print(stu_gra)
print("original list:")
while stu_gra:
    print(stu_gra.pop(),end=" ")