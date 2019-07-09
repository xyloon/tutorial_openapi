from pprint import pformat

stack=[]

def print_stack_before_operation(f):
    def method(*args, **kwargs):
        print("Current stack:", pformat(stack))
        f(*args, **kwargs)
        print("After operation:", pformat(stack))
    return method

def print_operation_name_and_parameter(f):
    def method(*args, **kwargs):
        print("Operation name:{0} {1}".format( f.__name__, (", parameter: {0}".format( pformat(*args, **kwargs)) if args or kwargs else "")))
        f(*args, **kwargs)
    return method

def print_spaceline(linecount):
    def wrapper(f):
        def method(*args, **kwargs):
            f(*args, **kwargs)
            for _ in range(linecount): print()
        return method
    return wrapper
        
@print_spaceline(1)
@print_stack_before_operation
@print_operation_name_and_parameter
def push(v):
    stack.append(v)

@print_spaceline(1)
@print_stack_before_operation
@print_operation_name_and_parameter
def multiply():
    a = stack.pop(-1)
    b = stack.pop(-1)
    stack.append(a*b)

@print_spaceline(1)
@print_stack_before_operation
@print_operation_name_and_parameter
def add():
    a = stack.pop(-1)
    b = stack.pop(-1)
    stack.append(a+b)


@print_spaceline(1)
@print_stack_before_operation
@print_operation_name_and_parameter
def pop():
    print("Poped ------------------->", stack.pop(-1))
    


opcodes={
    1: {
        "func": push,
        "pcount": 1
        },
    2: {
        "func": multiply,
        "pcount": 0
        },
    3: {
        "func": add,
        "pcount": 0
        },
    4: {
        "func": pop,
        "pcount": 0
        }
}
# 1+2*3+4 = 11
push(1)
push(2)
push(3)
multiply()
add()
push(4)
add()
pop()

print("=*"* 30)

codes=[1, 1,
       1, 2,
       1, 3,
       2,
       3,
       1, 4,
       3,
       4
]

while codes:
    code=codes.pop(0)
    params = []
    for _ in range(opcodes[code]['pcount']):
        params.append(codes.pop(0))
    opcodes[code]['func'](*params)


