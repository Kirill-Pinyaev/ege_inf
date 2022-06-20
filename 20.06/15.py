with open('24-196.txt') as f:
    data = f.read().rstrip()
    data = data.replace('ZX', '*').replace('ZY', '*')
    data = data.replace('ZX', '*').replace('ZY', '*')
    data = data.replace('X', ' ').replace('Y', ' ').replace('Z', ' ')
    data = data.split()
    print(len(max(data, key=len)))