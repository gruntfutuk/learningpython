import re
text = '''
ТЕЛЮЭБ

Вяжется по кругу, вокруг воздушных петель. Набивается
равномерно по ходу вязания, средней плотности.

1. ввп, начиная со второй петли от крючка 4сбн, Зсбн в
одну петлю, Зсбн, прибавка=12сбн

2. прибавка, Зсбн, 3 прибавки, Зсбн‚ 2 прибавки=18сбн

3.1сбн‚ прибавка, Зсбн‚ (1сбн, прибавка)-Зра3а‚ Зсбн‚
(1сбн, прибавка)-2раза=24сбн

4. 2сбн, прибавка, 3сбн‚ (2сбн‚ прибавка)-Зра3а‚ 3сбн‚
(2сбн‚ прибавка)-2раза=30сбн

5. Зсбн‚ прибавка, 3сбн‚ (3с6н‚ прибавка)-3раза‚ 3сбн,
(Зсбн, прибавка)-2раза=36сбн

6. 4сбн, прибавка, 3сбн, (4сбн‚ прибавка)-Зра3а‚ Зсбн,
(4сбн, прибавка)-2раза=42сбн

7. 21сбн, прикладываем ногу и провязываем вместе
6сбн, 6сбн, бсбн вместе с второй ногой, Зсбн=42сбн
'''

translation_table = {'прибавок': 'zunehmen',
                     'сбн': 'fM',
                     'пр': 'zun',
                     'Голова': 'Kopf',
                     'в кольцо': 'zur Runde schließen',
                     'по кругу': 'fM in alle Maschen',
                     'Ухо': 'Ohr',
                     '2сбн': '2 fM',
                     '3сбн': '3 fM',
                     '4сбн': '4 fM',
                     '6сбн': '6 fM',
                     'круг': 'Runde',
                     'ряда': 'mal',
                     'вл': 'LM',
                     'уб. убавка': 'zusammenhäkeln',
                     'пр. прибавка': '2 Maschen in eine',
                     'цифра кол-во СБН': '3 zusammenhäkeln',
                     '3в1 -3сбн в одну петлю': '3 Maschen in eine',
                     'cc': 'KM',
                     'голова': 'Kopf',
                     'кольцо': 'Ring',
                     'in next 2 st': 'in 2 Maschen',
                     'in next 8 st': 'in die nächsten 8 Maschen',
                     'уб': 'abn',
                     '6 sc in magic ring': '6 fM in den Fadenring',
                     'in the next': 'in die nächsten',
                     'sl st': 'KM',
                     'in all': 'in Alle',
                     'st': 'Masche',
                     'in next': 'in die nächsten',
                     'repeat 3 times': '3x wiederholen',
                     'repeat 4 times': '4x wiederholen',
                     'repeat 2 times': '2x wiederholen',
                     'fM in all 18 st': 'fM in alle 61 Maschen',
                     'в одну петлю': 'in eine Masche',
                     '3в1 - 3сбн в одну петлю': '3 Maschen in eine',
                     'кольцо': 'Ring',
                     'прибавка': 'zun.',
                     'cc': 'KM',
                     'соединительный столбик': 'Kettmasche',
                     'носик': 'Nase',
                     'ГОЛОВА.': 'Kopf',
                     'Основной цвет': 'Hauptfarbe',
                     'петлю': 'Masche',
                     'СБН': 'fM',
                     'приб.': 'zun.',
                     'приб.': 'zun.',
                     'приб.': 'zun.',
                     'приб.': 'zun.',
                     'раза': 'mal',
                     'Цвет рубашки': 'Farbe des Hemdes',
                     'ХВОСТИК': 'Schwänzchen',
                     'СБОРКА И ОФОРМЛЕНИЕ.': 'MONTAGE UND DESIGN.',
                     'УШКИ': 'Ohren',
                     'Отверстие стянуть.': 'Abnmaschen',
                     'раз': 'mal',
                     'во вторую': 'in die zweite',
                     'по другой стороне': 'auf der anderen Seite',
                     'Отверстие стянуть': 'Abketten',
                     'Правая рука.': 'rechte Hand',
                     'Набить тело.': 'Fülle den Körper.',
                     'ГОЛОВА.': 'Kopf',
                     'в.п': 'LM',
                     'Набить ручку.': 'Ausfüllen',
                     'приб.': 'Zun.',
                     'Не набивать. Верхние края сложить вместе и провязать': ' Die Ränder zusammen stricken',
                     'Правая рука.': 'rechte Hand',
                     'ТЕЛО.': 'Körper',
                     'ввп': 'nicht übersetzt',
                     'прибавок': 'zunehmen',
                     'сбн': 'fM',
                     'Зсбн': '3 fM',
                     'вместе с второй ногой': 'zusammen mit dem zweiten Bein',
                     '42сбн': '42 fM',
                     'прикладываем ногу и провязываем вместе': 'Befestigen Sie das Bein und binden Sie es zusammen',
                     'Зра3а': '3 x',
                     '-3раза': '3 x',
                     '21сбн': '21 fM',
                     '2раза': '2 x',
                     'нить': 'Faden',
                     'закрепи': 'befestigen',
                     'обрезатч': 'abschneiden',
                     'начиная со второй петли от крючка': 'beginnend mit der zweiten Masche von der Nadel aus',
                     'одну': 'eine',
                     'прибавки': 'Zun',
                     'средней плотности.': 'von mittlerer Dichte',
                     'в': 'in'}
