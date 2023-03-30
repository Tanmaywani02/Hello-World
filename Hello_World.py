import time

name = "hello world"
words = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
new_name = ""
ind = 0
flag = True
while flag:
    if name.lower() == new_name:
        # print(name)
        # break
        flag = False
    elif name[ind] == ' ':
        new_name += ' '
        ind += 1
    else:
        for i in words:
            if name.lower() == new_name:
                break
            else:
                print(new_name + i)
                time.sleep(0.05)
                
                if i == name[ind].lower():
                    new_name += i
                    ind +=1