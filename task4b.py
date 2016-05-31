class task4b:
    file = None
        
    def calcArea():
        count = 0
        #If file is not referenced yet, call enterFileName function 
        if task4b.file==None:
            task4b.enterFileName()
        #iterate through all lines in file to find coordinates
        for i in task4b.file:
            #Just a way to skip the first line in file as it is just a description data
            if count==0:
                count+=1
                continue
            #split the line using comma as seperator as that is the way it is arranged
            line = i.split(',')
            # uid = User Id
            uid = line[0]
            # uname = User Name
            uname = line[1]
            #Convert the rest(excluding first two elements) to list of floats using list comprehension 
            coordinates = [float(i) for i in line[2:]]
            #the first one is x1, second y1, third x2, fourth y2. So creating lists of x and y seperately
            x = coordinates[::2]
            y = coordinates[1::2]
            #Initializing area variable to zero
            area = 0
            #Using n to go till n-2 in the loop to get upto second last element as j+1 will evalute to n-1(last) element  
            # in the final loop.
            n = len(x)-1
            # Using Shoelace formula
            for j in range(n):
                area += (x[j]*y[j+1]) - (x[j+1]*y[j])
            #The final expression where last elements multiply with first ones
            area+=(x[n]*y[0]) - (x[0]*y[n])
            #Print the answer along with User Id and User Name
            print(uid+" "+uname+" "+str(area/2))
        task4b.file.close()    #Close the file

    def enterFileName():
        try:
            task4b.file = open(input("Enter the file path: "), 'r')
        except:
            print("Path not valid")
            exit()      

    def task4b_usage():
        print("Enter file name where file contains\nlist of space seperated coordinate values\neg.. x1 y1 x2 y2 ... xn yn")
        

if __name__ == "__main__":
    task4b.task4b_usage()
    task4b.calcArea()
