''' Beginner challenge.

Write a function that converts a string containing an ordered sequence of positive whole
numbers and number ranges to an ordered list of those numbers.

Number are separated with commas (and optional spaces) and number ranges are marked with
a - between two whole numbers (with optional spaces either side).

For bonus points, include validation, and handle out of order sequences and ranges.

State your assumptions (so interpret the challenge your way).

For example,

‘1-5, 7, 9, 10-13’ should convert to [1, 2, 3, 4, 5, 7, 9, 10, 11, 12, 13]
'''

# Stuart Moore's solution - no validation
def str_to_numlst(sample):
    ''' returns list of numbers from string of numbers and ranges of the format x-y
    separated by commas '''
    return [num for comma_sep in sample.split(',')
            for before, _, after in [comma_sep.partition('-')]
            for num in range(int(before), int(after or before) + 1)
            ]

# Stuart Moore's solution - with validation
def str_to_numlst_valid(sample):
    ''' returns list of numbers from string of numbers and ranges of the format x-y
    separated by commas, returns error message in ValueError if bad data given

    assumption: numbers returned should be unique '''
    result = []
    errmsg = ''
    source = "".join(sample.split())
    for comma_sep in source.split(','):
        before, hyphen, after = comma_sep.partition('-')
        if (not before or not before.isnumeric()) or \
                (hyphen and not after) or \
                (after and not after.isnumeric()):
            errmsg += f'   ***>> {comma_sep} bad int/range'
        else:
            start = int(before)
            fini = int(after) if after else start
            if start > fini:
                start, fini = fini, start
            for num in range(start, fini + 1):
                result.append(num)
    if errmsg:
        raise ValueError(errmsg)
    return sorted(set(result))


def Leo_Francisco_Simpao(data):
    stripped_data = [x.strip() for x in data.split(",")]
    ordered_list = []
    for i in stripped_data:
        if "-" in i:
            ls = list(map(int, i.split("-")))
            for x in range(ls[0], ls[-1] + 1):
                ordered_list.append(x)
        else:
            ordered_list.append(int(i))
    return ordered_list


def Ben_Cleary(data):
    import re

    class InvalidDigit(Exception):
        pass

    class OrderedSequenceGenerator:
        processed = []
        cleaned_payload = []

        def __init__(self, data):
            self.safety_check_and_process(data)

        def sorted(self):
            return sorted(self.processed)

        def safety_check_and_process(self, data):
            pattern = re.compile("^[0-9]{1,}?(-[0-9]{1,})?$")
            for item in list(map(lambda item: item.strip(), data.split(','))):
                if pattern.match(item):
                    self.cleaned_payload.append(item)
                else:
                    raise InvalidDigit(
                        f"'{item}' is not in correct format, please use XXX-XXX // X, where X is a positive integer")

        def check_range_values(self, item):
            if item[0] > item[1]:
                return [item[1], item[0]]
            elif item[0] == item[1]:
                return [item[0]]
            else:
                return [item[0], item[1]]

        def order(self):
            for item in self.cleaned_payload:
                if "-" in item:
                    r = self.check_range_values(
                        list(map(int, item.split('-'))))
                    if r.__len__() > 1:
                        [self.processed.append(x)
                         for x in range(r[0], r[1] + 1)]
                    else:
                        self.processed.append(r[0])
                else:
                    self.processed.append(int(item))

    sequence = OrderedSequenceGenerator(data)
    sequence.order()
    return sequence.sorted()


def Abhijit_Mukherjee(input_sequence):
    list_of_num = []
    for input in input_sequence.split(','):
        if len(input) > 1:
            for num in range(int(input.split('-')[0]), int(input.split('-')[1]) + 1):
                list_of_num.append(num)
        else:
            list_of_num.append(int(input))

    return list_of_num


def Carlos_Guillermo_Durazo(lst):

    def valid_range(val):
        import re
        tmp = re.findall('\d+-\d+', val)
        if len(tmp) == 1:
            val = val.split('-')
            tmp = tmp[0].split('-')
            if val[0] == tmp[0] and val[1] == tmp[1]:
                return True
        return False

    final_list = set()
    for i in lst.split(','):
        if len(i.split('-')) == 1:
            if i.replace(' ', '').isdigit():
                final_list.add(int(i.replace(' ', '')))
        else:
            tmp = i.replace(' ', '')
            if valid_range(tmp):
                tmp = tmp.split('-')
                for j in range(int(tmp[0]), int(tmp[-1]) + 1):
                    final_list.add(int(j))
    return list(final_list)


def Umar_Khan(Input_String):
  Output_list = []
  for elements in Input_String.split(','):
    Elements_contain_Number = False
    for num in elements:
      if num.isdigit():
        Elements_contain_Number = True
        break
    if Elements_contain_Number == True:
      new_element = elements.replace(" ", "")
      if '-' not in new_element:
        Sequence_Number = ''
        for k in new_element:
          if k.isdigit():
            Sequence_Number = Sequence_Number + k
        Output_list.append(int(Sequence_Number))
      else:
        Range_Number = []
        for k in new_element.split('-'):
          if k.isdigit():
            Range_Number.append(int(k))
        if len(Range_Number) >= 2:
          if Range_Number[0] > Range_Number[1]:
            Start = Range_Number[1]
            End = Range_Number[0] + 1
          else:
            Start = Range_Number[0]
            End = Range_Number[1] + 1
          for i in range(Start, End):
            Output_list.append(i)
        else:
          Output_list.append(Range_Number[0])
  return sorted(list(set(Output_list)))

def Pierre_Chiggles(NumericString):
  #print(NumericString)
  Index = 0
  Error = "Is not Integer"
  NewArray = []
  array = NumericString.split(",")
  while Index <= len(array)-1:
    Element = array[Index]
    if "-" in Element:
      Elements = Element.split("-")
      Element_1 = Elements[0].strip()
      Element_2 = Elements[1].strip()
      try:
        Element_1 = int(Element_1)
        Element_2 = int(Element_2)
      except:
        return Error
      Elements = []
      Elements.append(Element_1)
      Elements.append(Element_2)
      Elements.sort()
      Element = Elements[0]
      while Element <= Elements[1]:
        if Element not in NewArray:
          NewArray.append(Element)
        Element += 1
    else:
      Element = Element.strip()
      try:
        Element = int(Element)
      except:
        return Error
      if Element not in NewArray:
        NewArray.append(int(Element))
    Index +=1
    NewArray.sort()
  return NewArray

def Andre_Müller(seq, constructor=set):
    from contextlib import suppress

    def adv_range(seq):
        for element in seq.split(','):
            with suppress(ValueError):
                if '-' in element:
                    start, _, stop = element.partition('-')
                    start, stop = int(start), int(stop)
                    direction = 1 if start <= stop else -1
                    yield from range(start, stop + direction, direction)
                else:
                    yield int(element)

    retval = constructor(adv_range(seq))
    return sorted(retval)

def Zarren_Donovan_Spry(stringInput):
    unsortedList = []
    error = 0
    rawList = stringInput.split(",")
    for item in rawList:
        if "-" in item:
            num1,hyphen,num2 = item.partition("-")
            num1 = num1.strip(" ")
            num2 = num2.strip(" ")
            if num1.isnumeric() and num2.isnumeric():
                num1 = int(num1)
                num2 = int(num2)
                if num1 < num2:
                    for i in range(num1,num2 + 1):
                        unsortedList.append(i)
                elif num1 > num2:
                    for i in range(num2,num1 + 1):
                        unsortedList.append(i)
        removeNoise = item.strip(" ")
        if removeNoise.isnumeric():
            unsortedList.append(int(item))
    return sorted(list(set(unsortedList)))


def test_funcs(*funcs):
    import traceback
    tests = [('1-5,7,9,10-13', [1, 2, 3, 4, 5, 7, 9, 10, 11, 12, 13]),
             ('5, 10-6, 4-8,3', [3, 4, 5, 6, 7, 8, 9, 10]),
             ('1023,675,43, 23400-23395, 5-12', [5,6,7,8,9,10,11,12,43,675,1023,23395,23396,23397,23398,23399,23400]),
             ('1, 3 -5, 6-, -, 7, -9 , 16 - 20,23',
              [1, 3, 4, 5, 7, 16, 17, 18, 19, 20, 23]),
             ('2, 4, num, ;5, a-b', [2, 4])
             ]
    for func in funcs:
        print(f'\n\nTesting function: {func.__name__}\n')
        print('-----------')
        for test, assertion in tests:
            print(f'Testing: {test}')
            try:
                result = func(test)
            except ValueError as errmsg:
                print(errmsg)
            except Exception as e:
                print(f'ERROR: {traceback.format_exc()}')
            else:
                try:
                    assert sorted(set(result)) == assertion
                except AssertionError:
                    print(
                        f'*** ERROR -> for {test}\n\texpected {assertion},\n\treceived {result}')
                else:
                    print(result, end='')
                    if result != sorted(set(result)):
                        print(' ** result not ordered/unique')
                    else:
                        print()
            print('-----------')


if __name__ == "__main__":
    test_funcs(str_to_numlst, str_to_numlst_valid, Leo_Francisco_Simpao,
               Ben_Cleary, Abhijit_Mukherjee, Carlos_Guillermo_Durazo,
               Umar_Khan, Pierre_Chiggles, Andre_Müller,
               Zarren_Donovan_Spry)
