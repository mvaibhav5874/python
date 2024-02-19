import threading as mt
import time
list =[]

def enter():
    global list

    query = ''

    while query != 'stop':
        query = input('>>')
        list.append(query)

def output():
    while True:
        if len(list) > 0:
            if list[0] != 'stop':
                print(list[0])
                list.pop(0)
            else:
                break
        time.sleep(3)

t1=mt.Thread(target=enter)
t2=mt.Thread(target=output)

t1.start()
t2.start()
