from queue import Queue

def reverse_firat_k_ele(queue, k):

    if queue.qsize()<k or k<=0:
        print("inavalid")
        return 
    stack =[]

    for _ in range(k):
        stack.append()