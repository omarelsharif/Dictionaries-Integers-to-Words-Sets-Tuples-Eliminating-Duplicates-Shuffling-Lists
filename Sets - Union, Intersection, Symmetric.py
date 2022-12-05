


def intersection(first,last):
    firstset = set(first)
    lastset = set(last)
    intersection = firstset.intersection(lastset)
    #print("First set is: ,", firstset)
    print("Intersection: ", intersection)


def union(first,last):
    firstset = set(first)
    lastset = set(last)
    union = firstset.union(lastset)
    #print("First set is: ,", firstset)
    print("Union: ", union)
    

def symmetric(first, last):
    firstset = set(first)
    lastset = set(last)
    symmetric = firstset.symmetric_difference(lastset)
    print("Symmetric: ", symmetric)
    


def main(): 
  first = input("Enter a first name: ")
  last = input("Enter a last name: ")
  intersection(first, last)
  union(first, last)
  symmetric(first,last)


main()
