


def randomshuffle(lst):
    
    m = []
    m = lst.split(" ")
    m = list(m)
   # m[:] = lst
    
    for i in range(0, len(m)-1):
        i = int(i)
    import random
    for i in range(0,len(m)-1):
        x = random.randint(0,len(m)-1)
        temp = m[i]
        replace = m[x]
        m[x] = temp
        m[i] = replace
    m = [int(x) for x in m]
    print(m)
    

def main():
    lst = (input('Enter numbers: '))
 
    randomshuffle(lst)


main()
