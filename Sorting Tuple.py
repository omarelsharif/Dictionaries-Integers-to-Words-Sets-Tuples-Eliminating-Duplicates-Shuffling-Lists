






def sorting(tuples):
        tuples = list(tuples)
        tuples.sort()
        tuples = tuple(tuples)
        return (tuples) 


def main():
        nums = input("Enter numbers: ")
        
        splitnums = nums.split()
        splitnums  = [int(x) for x in splitnums]
        splitnums = tuple(splitnums)
        print("Before sorting:",splitnums)
        
        print("After sorting:", sorting(splitnums))



main() 
