class task4b:
    listOfCoordinates = list()
        
    def calcArea():
        count = 0
        if len(task4b.listOfCoordinates)<1:
            task4b.enterFileName()
        for i in task4b.listOfCoordinates:
            if count==0:
                count+=1
                continue
            line = i.split(',')
            uid = line[0]
            uname = line[1]
            coordinates = [float(i) for i in line[2:]]
            x = coordinates[::2]
            y = coordinates[1::2]
            area = 0
            n = len(x)-1
            for j in range(n):
                area += (x[j]*y[j+1]) - (x[j+1]*y[j])
            area+=(x[n]*y[0]) - (x[0]*y[n])
            print(uid+" "+uname+" "+str(area/2))
        task4b.listOfCoordinates.close()

    def enterFileName():
        try:
            task4b.listOfCoordinates = open(input("Enter the file path "), 'r')
        except:
            print("Path not valid")
            exit()      

    def task4b_usage():
        print("Enter file name where file contains\nlist of space seperated coordinate values\neg.. x1 y1 x2 y2 ... xn yn")
        

if __name__ == "__main__":
    task4b.task4b_usage()
    task4b.calcArea()
