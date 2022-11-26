score = input("Enter a score: ")
iscore = float(score)

try:
    if iscore >=0.9:
        print('A')
    elif iscore >=0.8:
        print('B')
    elif iscore >=0.7:
        print('C')
    elif iscore >=0.6:
        print('D')
    elif iscore <0.6:
        print('F')
except:
    iscore > 1.0

if iscore > 1.0:
    print('input number is out of range',)