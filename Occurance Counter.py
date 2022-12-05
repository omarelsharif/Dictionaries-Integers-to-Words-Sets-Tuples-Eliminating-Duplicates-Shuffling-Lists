




def counter(inputs):
    m = []
    m = inputs.split(" ")
    m = list(m) 
    nums = []

    for i in range (1,101):
        nums.append(str(i))

    counter = [0]*100
    
    for i in range(0,len(m)):
        for z in range(0,100):
            if  m[i] == nums[z]:
                y = int(nums[z])
                counter[y] +=  1

    for i in range(0, len(counter)):
        if counter[i] ==1:
            print(i, "occurs",counter[i],"time")
        elif counter[i] >1:
            print(i, "occurs",counter[i],"times")
            

def main():
    inputs = (input('Enter the integers between 1 and 100: '))
 
    counter(inputs)


main()
