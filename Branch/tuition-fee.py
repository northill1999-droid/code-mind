princing = 110
applicants = 10

actual_revenue = princing * applicants
expected_revenue = 3500

revenue_list = []
while True:
    princing -= 1
    applicants += 1
    actual_revenue = princing * applicants
    revenue_list.append(actual_revenue)
    if princing <= 0:
        break

for i in revenue_list:
    if i >= 3500:
        print(i)
        