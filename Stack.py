class Stack:

    def __init__(self):
        self.stak = []

    @property
    def isEmpty(self):
        if self.stak:
            return False
        else:
            return True

    def push(self, element):
        self.stak.append(element)

    def pop(self):
        return self.stak.pop()

    @property
    def peek(self):
        if self.stak:
            return self.stak[-1]
        else:
            return ''

    @property
    def size(self):
        return len(self.stak)


def validator(object: str):
    stack = Stack()
    yes = "Сбалансированно"
    no = "Несбалансированно"
    for el in object:
        if el == '(':
            stack.push('()')
        elif el == ')':
            if el in stack.peek:
                stack.pop()
            else:
                return print(object, no)
        elif el == '[':
            stack.push('[]')
        elif el == ']':
            if el in stack.peek:
                stack.pop()
            else:
                return print(object, no)
        elif el == '{':
            stack.push('{}')
        elif el == '}':
            if el in stack.peek:
                stack.pop()
            else:
                return print(object, no)
    if not stack.isEmpty:
        return print(object, no)
    return print(object, yes)


test_list = [
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}',
    '{{[()]}}',
    '}{}',
    '{{[(])]}}',
    '[[{())}]',
    '({[)}]',
    '())))((('
]

for test in test_list:
    validator(test)
