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
