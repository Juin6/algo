def solution(new_id):
    answer = ''
    
    new_id = new_id.lower() #1
    
    list = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f' , 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '_', '.']
    for i in new_id: #2
        if i in list:
            pass
        else:
            new_id = new_id.replace(i, '')
    
    while '..' in new_id:
        new_id = new_id.replace('..', '.') #3
    
    x = len(new_id)
    if new_id[0] == '.' and new_id[x-1] == '.':
        new_id = new_id[1:x-1]
    elif new_id[0] == '.':
        new_id = new_id[1:x]
    elif new_id[x-1] == '.':
        new_id = new_id[0:x-1] 
    
    if new_id == '': #5
        new_id = 'a'
    
    if len(new_id) >= 16: #6
        new_id = new_id[:15]
        if new_id[14] == '.':
            new_id = new_id[:14]
    
    while len(new_id) < 3:
        if len(new_id) == 1:
            new_id = new_id + new_id + new_id
        elif len(new_id) == 2:
            new_id = new_id + new_id[1]
            
    answer = new_id
    
    return answer