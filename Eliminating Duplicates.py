


def eliminateDuplicates(lst):
   # m = []
    #m[:] = lst
    m = lst.split()
   # m = list(m) 
    #m 
    final = []
    exists  = 0 
    for i in range(0,len(m)):
        for z in range(0,len(final)):
            if m[i]==final[z]:
                exists = 1
        if exists!=1:
            final.append(m[i])
        exists =0
    final = [int(x) for x in final]
    return(final)


def main():
    lst = input("Enter numbers: ")
    print('The distinct numbers are: ', eliminateDuplicates(lst))
    


main()
