#1
#import re
#print(re.findall(pattern='\d',string='vd0103fva0332r'))

#2
#import re
#a = re.findall(pattern='[A-Z]+|[А-Я]+', string='фываыфQWEQWERфцуацуаЙЦУЙЦЙЦУЙЦУ')
#print(a)

#3
#import re
#a=re.findall(pattern="r\b\w*а\d+\w*\b",string = "Привет32,своvndjj23")
#print(a)

import re
#1
#import re
#print(re.findall(pattern='\d',string='vd0103fva0332r'))

#2
#import re
#a = re.findall(pattern='[A-Z]+|[А-Я]+', string='фываыфQWEQWERфцуацуаЙЦУЙЦЙЦУЙЦУ')
#print(a)

#3
#import re
#a=re.findall(pattern="r\b\w*а\d+\w*\b",string = "Привет32,своvndjj23")
#print(a)

#4
#import re
#string = " Апельсин, banana, Кофе, Apple, Чай."
#pattern = r'\b[А-ЯA-Z][а-яA-яA-Za-z]*\b'
#matches = re.findall(pattern,string)
#print(matches)

#ДОМАШКА НИЖЕ

#1
#import re
#a='С227НА777 КУ22777 Т22В7477 М227К19У9 С227НА777'
#def check_license_plate(plate):
#taxi_pattern=r'[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}'
#    for plate_1 in plate.split():
#        match_1=re.fullmatch(pattern=private_car,string=plate_1)
#        match_2=re.fullmatch(pattern=taxi_pattern, string=plate_1)
#        if match_1 is not None:
#           print('private_car')
#        elif match_2 is not None:
#            print('taxi_pattern')
#        elif match_1 is None and match_2 is None:
#            print('не номер')
#check_license_plate(a)

#2
#import re
#def count_words(input_string):
#    russian_words = re.findall(pattern=r'\b[а-яА-Я]+\b', string=input_string)
#    return len(russian_words)

#input_string = "Он --- серо-буро-малиновая редиска!! >>>:-> А не кот. www.kot.ru"
#russian_word_count = count_words(input_string)
#print("Количество слов на русском языке в строке:", russian_word_count)

#3
import re

text="Уважаемые! Если вы к 09:00 не вернете чемодан, то уже в 09:00:01 я за себя не отвечаю. PS. С отношением 25:50 всё нормально!"
pattern_first=r'\b[0-1][0-9]:[0-5][0-9]|2[0-3]:[0-5][0-9]\b'
pattern_second=r'\b[0-1][0-9]:[0-5][0-9]:[0-5][0-9]|2[0-3]:[0-5][0-9]:[0-5][0-9]\b'

result= re.sub(pattern=f"{pattern_second}|{pattern_first}", string=text, repl="(TBD)")

print(result)