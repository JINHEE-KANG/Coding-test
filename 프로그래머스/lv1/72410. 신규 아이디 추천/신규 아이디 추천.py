def solution(new_id):
    new_id = new_id.lower()
    
    for l in new_id:
        if not l.isalnum() and l not in ['-','_','.']:
            new_id = new_id.replace(l,'')
    
    while '..' in new_id:
        new_id = new_id.replace('..','.')
    
    if new_id.startswith('.') and new_id.endswith('.'): 
        new_id = new_id[1:-1]
    elif new_id.startswith('.'): 
        new_id = new_id[1:]
    elif new_id.endswith('.'): 
        new_id = new_id[:-1]
        
    if len(new_id)==0: 
        new_id = 'a'
    elif len(new_id)>=16: 
        new_id = new_id[:15]
        if new_id.endswith('.'): 
            new_id = new_id[:-1]
    
    if len(new_id)<=2:
        t = new_id[-1]*(3-len(new_id))
        new_id += t
            
    
    return new_id