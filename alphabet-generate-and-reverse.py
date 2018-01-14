# print the reverse of the alphabet
alphabet=[chr(i) for i in range(ord('a'),ord('z')+1)]  # list of a .. z
zulubet=alphabet[::-1] # reverse list
print(''.join(zulubet)) # join the list entries into one string and print	