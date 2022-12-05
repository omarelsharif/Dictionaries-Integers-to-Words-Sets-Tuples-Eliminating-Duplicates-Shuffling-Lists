




def main():
    dictionary = {} 
    run = "run"
    while run == "run":
        x = input("Enter a coutnry and a capital comma seperated (Q to Quit): ")
        if x== "Q":
            run = "stop"
        else:
            x = x.split(",")
            dictionary[x[0]] = x[1]

    keys = dictionary.keys()
    keyslist = list(keys)
    keyslist.sort()
    print(" ")

    
    print("COUNTRY              CAPITAL")
    
    for i in keyslist:
        z = "{:20s}".format(i)
        x = "{:20s}".format(dictionary[i])
        print(z, x)
          
    
        #print(x)
 
        




main() 
