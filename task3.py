subjectsDict = {}

with open('Учебные предметы.txt', 'r', encoding='utf-8') as file:
    try:
        lines = file.readlines()
    except IOError: print('Возникла ошибка чтения файла\n')

for line in lines:
    parts = line.split(': ')
    if len(parts) == 2:
        name, schedule = parts
        hours = schedule.split(' ')
        totalHours = 0
        for hour in hours:
            if '(лк)' in hour:
                hour = int(hour.replace('(лк)',''))
                totalHours += hour
            elif '(пз)' in hour:
                hour = int(hour.replace('(пз)', ''))
                totalHours += hour
            elif '(лр)' in hour:
                hour = int(hour.replace('(лр)',''))
                totalHours += hour
        subjectsDict[name] = totalHours
print(subjectsDict)


