def Order(Input_String):

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


def test_funcs(*funcs):
  import traceback
  tests = [('1-5,7,9,10-13', [1, 2, 3, 4, 5, 7, 9, 10, 11, 12, 13]),
           ('5, 10-6, 4-8,3', [3, 4, 5, 6, 7, 8, 9, 10]),
           ('1023,675,43, 23400-23395, 5-12',
            [5, 6, 7, 8, 9, 10, 11, 12, 43, 675, 1023, 23395, 23396, 23397, 23398, 23399, 23400]),
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
  test_funcs(Order)
