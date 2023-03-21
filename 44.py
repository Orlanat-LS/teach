import json
import datetime

dir = "test.json"

with open(dir, "r", encoding="utf-8") as r:
    js = json.load(r)
    f_name = js["file name"]

    print(js)
    file = open(f_name, "r", encoding="utf-8")
    data = file.read().split('\n')
    file.close()
    print(data)

    index = 0 # Количество найденных предложений
    text = [] # Массив предложений

    # Поиск по всем предложениям
    for lines in data:
        for word in js["words"]: # Проверить наличие всех слов
            if word not in lines: # Условия прерывания
                break

        # Все слова в предложении найдены
        else:
            # Если длина предложения соответствует критериям отбора и не превышен лимит записи
            # min_len: 20
            # min_len: 200
            # num: 5
            if len(lines) >= js["example minimum length"] & len(lines) <= js["example minimum length"] & index <= js["number of examples"]:
                # Сохранить предложение
                text.append(lines)
                index += 1

    # Формирование результата
    res = {
              "count": index,
              "text": text,
              "time": {
                           "day":   datetime.datetime.now().day,
                           "month": datetime.datetime.now().month,
                           "year":  datetime.datetime.now().year
                      }
         }

    # Сохранение результирующего JSON файла
    with open("result.json", "w") as w:
          json.dump(res, w, indent=4, ensure_ascii=False)