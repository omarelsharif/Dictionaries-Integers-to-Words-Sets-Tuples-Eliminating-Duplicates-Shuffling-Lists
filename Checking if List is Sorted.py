



def isSorted(lst):
    m = lst.split()
    z = 0
    m = list(m)
    m = [int(x) for x in m]
    #print(m)
    
    for i in range(0,len(m)-1):
        
        if m[i] > m[i+1]:
            z = 1
    if z == 1:
        print("The list is not sorted")
    if z!=1:
        print("The list is already sorted")  


def main():
    lst = input("Enter numbers: ")
    isSorted(lst)

main()
