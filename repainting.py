needed_qul_nylon = float(input())
needed_qul_paint = float(input())
qul_thin_per_lit = float(input())
total_hours = float(input())
saf_nylon = 1.50
paint_per_lit = 14.5011
thin = 5
more_nylon = 2
more_paint = 1.1
bags = 0.40
nylon = (needed_qul_nylon + 2) * saf_nylon
paint = ((needed_qul_paint + more_paint) * paint_per_lit)
sumThin = qul_thin_per_lit * thin
finalTax = (nylon + paint + bags + sumThin)
by_hours = ((finalTax * 0.3) * total_hours)
print(by_hours + finalTax)
