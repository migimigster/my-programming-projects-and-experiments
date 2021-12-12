stack=[]
program_done = False
while not program_done:
    z=input("Push or Pop? Type done to end program ").lower()
    push_done=False
    pop_done = False
    if z=="push":
        while not push_done:
            x=input("Push what number? ")
            stack.append(x)
                
            print(stack, len(stack))
            s=input("Will you push again? y or n? ")
            if s=="n":
                push_done = True
    elif z=="pop":
        if not stack:
            print("Stack is empty")
            pop_done = True
        while not pop_done:
            if not stack:
                print("Stack is now empty")
                pop_done = True
            else:
                print(stack.pop())
                popp=input("Are you going to pop again? y or n? ")
                if popp=="n":
                    pop_done = True
    elif z=="done":
        program_done = True