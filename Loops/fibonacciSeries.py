num = int(input("Enter the number: "))

series = [0, 1]

for i in range(2, num):
    series.append(series[i - 2] + series[i - 1])

print(series)