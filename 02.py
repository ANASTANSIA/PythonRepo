"""
Prints Letter A
"""
size=eval(input('Height:'))

for i in range(size):
    for j in range((size//2)):
        if((j == 0 or j== size//2) and i !=0 or i==0 and j!=0 and j !=size//2 or i==size//2):
            print("*", end = "")
        
        else:
            print("" ,end= "")

    print()
            
                   
                   
