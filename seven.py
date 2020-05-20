def change(line):
    if(line.find('not')>0 and line.find('poor')>0):
        print(line.replace(line,'The lyrics is good!'))
    else:
        print(line) 
change('The lyrics is not that poor!')
change('The lyrics is poor!')
