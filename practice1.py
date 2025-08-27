#with open("practice.txt","r") as f:
#    data= f.read()

#new_data = data.replace("Java", "Python")
#print(new_data)

#with open("practice.txt","r") as f:
#    f.write(new_data)

def check_for_line():
    word="learning"
    data=True
    Line_no=1
    with open("practice.txt") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(Line_no)
            return 1
            Line_no +=1
    return -1

check_for_line()
