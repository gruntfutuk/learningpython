import csv, time
 
with open('parts.txt', 'r') as f:
    fieldnames = ('PartID', 'Partname', 'PartCost')
    parts = list(csv.DictReader(f.readlines(), fieldnames=fieldnames, skipinitialspace=True))
 
with open('products.txt', 'r') as d:
    fieldnames = ('BikeID', 'BikeName')
    products = list(csv.DictReader(d.readlines(), 
                                   fieldnames=fieldnames, 
                                   restkey='BikeParts', 
                                   skipinitialspace=True))
    
def get_name(ID):
    try: 
        if ID.startswith('bike'):
            for row in products:
                if row['BikeID'] == ID:
                    name = row['BikeName']
        else:
            for row in parts:
                if row['PartID'] == ID:
                    name = row['Partname']
        return name
    except UnboundLocalError:
        return 'Invalid ID'

def parts_cost(bike_id):
    try:
        for row in products:
            if row['BikeID'] == bike_id:
                cost = 0
                for item in row['BikeParts']:
                    part_id, qty = item.split(':')
                    for row in parts:
                        if part_id == row['PartID']:
                            cost += int(row['PartCost']) * int(qty)
        return cost
    except UnboundLocalError:
        return 'Invalid ID'

def load_parts(textfile):
    parts_file = open(textfile, 'r')
    parts = parts_file.readlines()
    parts_file.close()
    return parts

parts_data = load_parts('parts.txt')

partNames = {}
partPrices = {}
    
for line in parts_data:
    splitted_line = line.split(',')
    if len(splitted_line) == 1:
        continue
    ID = splitted_line[0].strip()
    Name = splitted_line[1].strip()
    Price = splitted_line[2].strip()
    
    partNames[ID] = Name
    partPrices[ID] = Price
    
#############################################
#
# First Name: Royce
# Last  Name: Jamie
#
#############################################


##def load_parts(textfile):
##    parts_file = open(textfile, 'r')
##    parts = parts_file.readlines()
##    parts_file.close()
##    return parts
##
##def load_products(textfile):
##    products_file = open(textfile, 'r')
##    products = products_file.readlines()
##    products_file.close()
##    return products
##
##parts_data = load_parts('parts.txt')
##products_data = load_products('products.txt')
##
##partNames = {}
##
##partPrices = {}
##
##productNames = {}
##
##productParts = {}
##
##
##for line in parts_data:
##    splitted_line = line.split(',')
##    if len(splitted_line) == 1:
##        continue
##    ID = splitted_line[0].strip()
##    Name = splitted_line[1].strip()
##    Price = splitted_line[2].strip()
##    
##    partNames[ID] = Name
##    partPrices[ID] = Price
##
##
##
##for line in products_data:
##    splitted_line = line.split(',')
##    if len(splitted_line) == 1:
##        continue
##    ID = splitted_line[0].strip()
##    Name = splitted_line[1].strip()
##    Price = splitted_line[2].strip()
##    
##    productNames[ID] = Name
##    productParts[ID] = Price
##    
##
##for x in parts_data:
##     print(x)
##     print('-------------------------------')
##
run = True

while run:
    command1 = input("Are you looking for a Part or a Product?\n")
    
    if command1 == 'product':
        command2 = input("What is the ID of the part you're looking for?\n")
        time.sleep(0.3)
        print(" ")
        print(" ")
        print("############################")
        print("## This is a", get_name(command2))
        print("## It costs", parts_cost(command2), 'cents')
        print("############################")
        print(" ")
        print(" ")
        response = input("Are you looking for another part? Yes/No\n")
        if response == ("No"):
            run = False
        else:
            continue
            
        
    if command1 == 'part':
        command2 = input("What is the ID of the product you're looking for?\n")
        time.sleep(0.3)
        print(" ")
        print(" ")
        print("############################")
        print("## This is a", partNames[command2])
        print("## It costs", partPrices[command2], 'cents')
        print("############################")
        print(" ")
        print(" ")
        response = input("Are you looking for another part? Yes/No\n")
        if response == ("No"):
            run = False
        else:
            continue
        

    
        
        


        
        
