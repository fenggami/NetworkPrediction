import numpy as np
import pandas as pd

def transformSolution():
    data = pd.read_csv('../data/solution_rf.csv')
    f = lambda x: x/x.max()
    data.apply(f)
    return data

def transform():
    readFile=open('../data/solution_rf.csv','r')
    writeFile=open('../data/solution/solution_rf.csv','w')
    next(readFile)
    for line in readFile:
        try:
            data=[float(d) for d in line.split(',')]
            maxIndex = data.index(max(data[1:]))
            for i in range(1,len(data)):
                if i == maxIndex:
                    data[i] = 1
                else:
                    data[i] = 0
            data = [str(d) for d in data]
            writeFile.write(','.join(data))
            writeFile.write('\n')
        except:
            print(line)


    readFile.close()
    writeFile.close()

if __name__ == "__main__":
    transform()



