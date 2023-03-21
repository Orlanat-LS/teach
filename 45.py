import json
import nltk
import datetime

dir()
nltk.download('punkt')

# Разбить текст файла на строки
def NLTK(dir):
    print(dir)
    file = open(dir, "r", encoding="utf-8").read()
    line = nltk.sent_tokenize(file, language="english")
    return line

# Сформировать результирующий JSON файл
def RESULT(dir):
    with open(dir, "r", encoding="utf-8") as r:
        js = json.load(r)
        data = NLTK(js["file name"])
        print(data)
        index = 0 # Количество найденных предложений
        text = [] # Массив предложений

        # Поиск по всем предложениям
        for lines in data:
            for word in js.get("words"): # Проверить наличие всех слов
                if word not in nltk.word_tokenize(lines): # Условия прерывания
                    break

            # Все слова в предложении найдены
            else:
                # Если длина предложения соответствует критериям отбора и не превышен лимит записи
                # min_len: 20
                # min_len: 200
                # num: 5
                if len(lines) >= js.get("min_len") & len(lines) <= js.get("min_len") & index <= js.get("num"):
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


RESULT("test.json")
