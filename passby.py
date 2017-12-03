# Confused by way variables are passed in Python
# I know pass-by-value and pass-by-reference do not apply
# but explanations I have found are not making sense
# to me.

# I have created a very simple script to help me illustrate
# what I am confused by

# I create a list called dinner with a couple of menu items
# pass that to a function, that adds two items
# then attempts to completely replace the menu
# the replaced menu is returned

# What happens?
# The orignal list has two items added by the function
# but the menu (list contents) are NOT replaced
# by the function alternative, but that alternative
# is returned by the function

# So, it seems that I can change the object referenced by the
# passed variable, but if I assign new values to the local
# variable, then I effective create a reference to a new object

def meal(plate):
    plate.append('eggs')
    plate.append('beans')
    plate = ['tofu', 'soya eggs', 'nuts']
    return plate

dinner = ['bacon', 'sausage']
veggie = meal(dinner)
print("Dinner: {}.".format(dinner))
print("Veggie: {}.".format(veggie))
