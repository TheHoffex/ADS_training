
class node:
    def __init__(self, val):
        self.val = val
        self.head = None

class singlelinkedlist:
    def __init__(self):
        self.head = None

    def add(self, val):
        if self.head == None:
            self.head = node(val)
            return
        h = self.head
        while h.head != None:
            h = h.head
        h.head = node(val)

    def display(self):
        h = self.head
        while h != None:
            print(h.val)
            h = h.head

    def remove(self, idx):
        h = self.head
        for i in range(idx - 1):
            h = h.head
        to_del = h.head
        h.head = h.head.head
        del to_del

def main():
    res = '110'

    res = list(res)
    res = [int(ele) for ele in res]
    res.reverse()
    print(res)
    return_val = 0
    for i, val in enumerate(res):
        print(val)
        if val == 1:
            return_val += 2**i

    return return_val


if __name__ == '__main__':
    main()