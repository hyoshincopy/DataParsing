import csv

f = open('./incheon.csv', 'r')
data = csv.reader(f)

header = next(data)
max_temp = -999
for row in data:
    if row[-1] == '':
        row[-1] = -999
    row[-1] = float(row[-1])
    if max_temp < row[-1]:
        max_temp = row[-1]
        max_data = row[0]


print('기상 관측 이래, 인천의 최고 기온이 가장 높았던 날은', max_data, ' 이고', max_temp, '도 이다')
f.close()
