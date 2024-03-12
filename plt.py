import matplotlib.pyplot as plt
def divison(a, b):
    return a / b

def inverse(x):
    return divison(1, x)

def main():
    for i in range(10):
        print(i, inverse(i))
try :
    main()
except Exception as e:
    print(e)

