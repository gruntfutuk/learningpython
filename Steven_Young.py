def Steven_Young(input_data):  # This will test data

    import re

    def generate_list(input_data):  # This will create the list
        list_len = len(input_data)
        range_list = re.findall('[0-9]+[-]+[0-9]+', input_data)
        formatted_list = []
        try:  # If there is a range, this will add the range to the list
            for j in range(0, 2):
                templist = re.findall('[0-9]+', range_list[j])
                inttemplista = int(templist[0])
                inttemplistb = int(templist[1]) + 1
                for i in range(inttemplista, inttemplistb):
                    formatted_list.append(i)
        except:
            pass
        #  The script here will add every missing number to the list
        temp_nonrange_list = re.findall('[0-9]+', input_data)
        temp_nonrange_list_len = len(temp_nonrange_list)
        for k in range(0, temp_nonrange_list_len):
            inttemplist = int(temp_nonrange_list[k])
            if inttemplist in formatted_list:
                continue
            else:
                formatted_list.append(inttemplist)
                continue
        return (formatted_list)

    input_data = str(input_data)
    if input_data == None or input_data == "":
        print("There is no data.")
        return
    abc_check = re.findall('[a-z][A-Z]*', input_data)
    if len(abc_check) > 0:
        print("[]")
        return
    formatted_list = generate_list(input_data)
    formatted_list.sort()
    print(formatted_list)


''' ******************************
    ***                        ***
    ***          TEST          ***
    ***                        ***
    ****************************** '''

from test import test_funcs

if __name__ == "__main__":
    test_funcs(Steven_Young)
