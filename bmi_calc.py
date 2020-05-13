qw = ["df", "sd", "er", "py"]
print("sd" in qw)
check = "sd" in qw
if check:
    print(qw.index("sd", 0, 4))
else:
    print("sd is not in qw list")

qw = ["df", "sd", "er", "py"]
print("sd" in qw)
if "sd" in qw:
    print(f'"sd" is in position {qw.index("sd", 0, 4)} in list qw')
else:
    print("sd is not in qw list")