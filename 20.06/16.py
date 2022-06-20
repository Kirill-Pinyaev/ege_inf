with open('24-197.txt') as f:
    s = f.read().rstrip()
    s = s.replace('ZXY', '*').replace('ZYX', '*')
    s = s.replace('ZXY', '*').replace('ZYX', '*')
    s = s.replace('ZXY', '*').replace('ZYX', '*')
    s = s.replace('X', ' ').replace('Y', ' ').replace('Z', ' ')
    s = s.replace('X', ' ').replace('Y', ' ').replace('Z', ' ')
    s = s.split()
    print(len(max(s, key=len)))