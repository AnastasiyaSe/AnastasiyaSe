

class Stack:
    def __init__(self):
        self.list = []

    def isEmpty(self):
        return self.list == []

    def push(self, list):
        self.list.append(list)

    def pop(self):
        return self.list.pop()

    def peek(self):
        return self.list[len(self.list) - 1]

    def size(self):
        return len(self.list)

se = '}{}'
es = se[::-1]
s=Stack()
for i in se:
    s.push(i)


a = Stack()
for i in es:
    a.push(i)

count = 0

for i in range(len(se)-1):
   if (a.peek() + s.peek()) =='()' or (a.peek() + s.peek()) =='[]' or (a.peek() + s.peek()) =='{}':
       count += 1

if count == len(se)-1:
    print('balance')
else:
    print('not balance')




