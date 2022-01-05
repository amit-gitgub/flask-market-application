

def defangIP(ip):
    ip.split('.')
    splitAddress = ip.split('.')
    seperator = "[.]"
    newAddess = seperator.join(ip)
    print(splitAddress)
    print(newAddess)

defangIP("10.5.7.19")