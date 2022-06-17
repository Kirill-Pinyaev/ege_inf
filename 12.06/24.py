with open('8_24.txt') as f:
    data = f.read().rstrip()
    while 'AB' in data or 'AD' in data:
        if 'AB' in data:
            data = data.replace('AB', '*')
        else:
            data = data.replace('AD', '&')
    data = data.replace('A', ' ').replace('B', ' ').replace('D', ' ')
    data = data.replace('A', ' ').replace('B', ' ').replace('D', ' ')
    data = data.split()
    print(len(max(data, key=len)))