import time
def count(start,end = 0):#Start argument(positional) is before end(default argument)
    for x in reversed(range(end,start+1)):
        print(x)
        time.sleep(0.5)
    print("Done!")
count(20)

def hello(greeting,title,first,last):
    print(f"{greeting} {title} {first} {last}")
hello("Hello", title ="Mr.", last = "Singh", first = "Ranveer")