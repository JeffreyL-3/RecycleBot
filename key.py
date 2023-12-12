mykey = ''

def getKey():
    return mykey
def setKey(newKey):
    global mykey  # Declare mykey as a global variable
    mykey = str(newKey)