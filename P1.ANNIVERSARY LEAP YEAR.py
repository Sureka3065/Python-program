date=input("enter date:")
d1=date.split('/')
l1=list(map(int,d1))
year=l1[2]
if year%4==0 or year%100!=0 and year%400==0:
    print("it is an leap year")
    print("the next leap year is:",year+4)
else:
    print("it is not a leap year")
    for i in range(1,5):
        year-=i
        if year%4==0 or year%100!=0 and year%400==0:
            print("the previous leap year is:",year)
