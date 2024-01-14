Dep = int(input())
Month = float(input())
YearsPercent = float(input())
years = YearsPercent/100
TotalSum = Dep + (Month * ((Dep * years)/12))
print(TotalSum)

