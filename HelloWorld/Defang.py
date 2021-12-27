#Defang the IP address

def change_ip(address):
    split_add = address.split(".")
    print(split_add)
    New_add = ""
    seperator = "[.]"
    New_add = seperator.join("amit")
    return New_add


defang_add = change_ip("37.28.9.145")
print(defang_add)
