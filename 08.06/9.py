with open('24.txt') as f:
    data = f.read()
    data = data.replace('XY', 'X Y').replace('XZ', 'X Z').replace('YX', 'Y X').replace('YZ', 'Y Z').replace('ZX', 'Z X'.replace('ZY', 'Z Y'))
    data = data.replace('XY', 'X Y').replace('XZ', 'X Z').replace('YX', 'Y X').replace('YZ', 'Y Z').replace('ZX', 'Z X'.replace('ZY', 'Z Y'))
    data = data.split()
    print(len(max(data, key=len)))