#Write your code here in python 


while True:
    x=input('enter the number')
    
    if x.upper()=='EXIT':
        break

    try:
        marks=int(x)
        if 90<=marks<=100:
            print("A")
        elif 75<=marks<=89:
            print('B')
        elif 60<=marks<=74:
            print('C')
        elif 40<=marks<=59:
            print('D')
        elif 0<=marks<40:
            print('F')
        else:
            print('invalid input')
    except ValueError:
        print('invalid')
    
