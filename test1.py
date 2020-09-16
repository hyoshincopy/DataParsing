import csv
import matplotlib.pyplot as plt

f = open('./incheon.csv', 'r')
data = csv.reader(f)
header = next(data)
max_temp = -999
high_temp = []
low_temp = []
year = []


for row in data:
    if row[0][5:10] == "05-11":
        if row[-1] == '':
            continue
        if row[-2] == '':
            continue
        year.append(row[0])
        high_temp.append(float(row[-1]))
        low_temp.append(float(row[-2]))

plt.rc('font', family='Malgun Gothic')
plt.title("birthday")
plt.plot(high_temp, color='hotpink', label='최고기온')
plt.plot(low_temp, color='b', label='최저기온')
plt.legend()
plt.show()


# for row in data:
#     if row[-1] == '':
#         row[-1] = -999
#     row[-1] = float(row[-1])
#     if max_temp < row[-1]:
#         max_temp = row[-1]
#         max_data = row[0]


# plt.title('plotting')
# plt.plot([0, 2.5, 5, 7.5, 10, 12.5, 15, 17.5, 20],
#          color='b', linestyle='--', label='범례1')
# plt.plot([16, 18, 20, 22, 24, 26, 28, 30],
#          color='k', ls=':', marker='o', label='범례2')
# plt.show()


f.close()
