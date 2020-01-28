from textwrap import TextWrapper as TW  # to indent river descriptions

wrapper = TW(width=60, initial_indent = ' '*30, subsequent_indent = ' '*25)

with open('river_details.txt') as file:
    river_details = file.read()

rivers = {river: (where,size,desc)
            for r in river_details.split('\n')
            for river, where, size, desc in [r.split(' | ')]}

for river, (where, size, desc) in rivers.items():
    desc_tw = wrapper.wrap(text=desc)
    print(f'\n\n{river:<10} - {where:<15} {size:>30}\n')
    print(*desc_tw, sep='\n')
    print(f'\n{"-"*70}')
