

def print_file(file_name):
    file = open(file_name, 'r', encoding='utf-8')
    messang = ''
    for w in file:
        messang += w
    
    return messang