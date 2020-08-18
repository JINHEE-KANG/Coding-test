def solution(s):
    if s[0]==')': return False
    
    op,ed = 0,0
    for i in range(len(s)):
        if s[i]=='(': 
            if op!=ed:
                print(f'op:{op},ed{ed},s[i]:{s[i]}')
                return False
            else:
                op+=1
                print(f'op:{op},ed{ed},s[i]:{s[i]}')
        else:
            ed+=1
            print(f'op:{op},ed{ed},s[i]:{s[i]}')
    print(f'op:{op},ed{ed},s[i]:{s[i]}')
    return True
