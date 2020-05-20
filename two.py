def find(year):
    if (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
        print('True')
    else:
        print('False')
if __name__ == "__main__":
    find(int(input()))
