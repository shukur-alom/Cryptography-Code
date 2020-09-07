user_mind = int(input('1. Code\n2.Decode\nChoose one : '))
new_line = 0
if user_mind == 1:
    user_input = input("Write some thing : ")
    for i in user_input:
        asci = ord(i)
        print(hex(asci),end=",")
elif user_mind == 2:
    user_input = input("Code : ")
    user_input_list = user_input.strip().split(',')
    if user_input_list[-1] == "":user_input_list.pop() 
    for i in user_input_list:
        hx = int(i,0)
        print(chr(hx),end="")
print('\n')