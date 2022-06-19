with open('24_100622.txt') as f:
    data = f.read()
    data = data.replace('AB', 'A B').replace('BA', 'B A').replace('CD', 'C D').replace('BC', 'B C')
    data = data.replace('AB', 'A B').replace('BA', 'B A').replace('CD', 'C D').replace('BC', 'B C')
    data = data.split()
    print(len(max(data, key=len)))