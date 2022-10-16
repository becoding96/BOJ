def push(item, size):
    global top
    top += 1
    if top == size:
        print('overflow!')
    else:
        stack[top] = item


def pop():
    global top
    if top == -1:
        return 'underflow'
    else:
        top -= 1
        return stack[top + 1]


size = 10
stack = [0] * size
top = -1

push(10, size)      # push
push(20, size)      # push
print(pop())        # pop
print(pop())
print(pop())
push(30, size)      # push
print(pop())
