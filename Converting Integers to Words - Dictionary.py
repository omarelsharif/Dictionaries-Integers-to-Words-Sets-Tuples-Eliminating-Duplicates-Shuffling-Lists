







def convert(x):
    numbers = {'0':'zero','1':'one','2':'two','3': 'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
    m = []
    m[:] = x
    for i in range(0, len(m)):
        z = m[i] 
        print(numbers[z], end = " ")

    
def main():
    x =  input("Enter an integer to convert to words: ")
    convert(x)

main()
