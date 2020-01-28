class login():

    def __init__(self, id, pas):
        self.id = id
        self.pas = pas

    def check(self, id, pas):  # you missed self
        if(self.id == id and self.pas == pas):
            print("Login success!")
            return True
        else:
            return False

log = login("admin","admin")
if log.check(input("Enter Login ID:"), input("Enter password: ")):
    print("Login Page")
else:
    print("Access not allowed")
