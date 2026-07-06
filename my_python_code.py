temperatures = [35, 25, 26, 25, 29, 27, 38]

total = sum(temperatures)
average = total / len(temperatures)
print(average)

for i, t in enumerate(temperatures):
    print(f"วันที่ {i + 1} มีค่า {t} องศา")


def classify_temp(t, avg):
    # if t > avg:
    #     return "ร้อน"
    # else:
    #     return "เย็น"

    return "ร้อน" if t > avg else "เย็น"

print(classify_temp(30, average))

import pandas as pd

df = pd.read_csv("pokemon.csv")
print(df.head())