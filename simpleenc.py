#The encryption key for the caesar cypher
encryptionKey=16


#Caesar Cypher Encryption
def passwordEncrypt (unencryptedMessage, key):

    #We will start with an empty string as our encryptedMessage
    encryptedMessage = ''
    #For each symbol in the unencryptedMessage we will add an encrypted symbol into the encryptedMessage
    for symbol in unencryptedMessage:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            encryptedMessage += chr(num)
        else:
            encryptedMessage += symbol
    return encryptedMessage


def loadPasswordFile(fileName):
    with open(fileName, newline='') as csvfile:
        passwordreader = csv.reader(csvfile)
        passwordList = list(passwordreader)
    return passwordList


def savePasswordFile(passwordList, fileName):
    with open(fileName, 'w+', newline='') as csvfile:
        passwordwriter = csv.writer(csvfile)
        passwordwriter.writerows(passwordList)


messageorg = "Mary had a little lamb. It's fleece as white as snow."
messageenc = passwordEncrypt(messageorg, encryptionKey)
messagerec  = passwordEncrypt(messageenc, -encryptionKey)
print(f'\n\norg: >{messageorg}<\nenc: >{messageenc}<\nrec: >{messagerec}<\n')
