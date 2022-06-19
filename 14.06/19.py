with open('24_ABCEF.txt') as f:
    data = f.read().rstrip()
    data = data.replace('AF', '*').replace('AC', '*').replace('AD', '*').replace('EF', '*').replace('EC', '*').replace('ED', '*')
    data = data.replace('AF', '*').replace('AC', '*').replace('AD', '*').replace('EF', '*').replace('EC', '*').replace('ED', '*')
    data = data.replace('AF', '*').replace('AC', '*').replace('AD', '*').replace('EF', '*').replace('EC', '*').replace('ED', '*')
    data = data.replace('A', ' ').replace('C', ' ').replace('D', ' ').replace('E', ' ').replace('F', ' ')
    data = data.replace('A', ' ').replace('C', ' ').replace('D', ' ').replace('E', ' ').replace('F', ' ')
    data = data.split()
    print(len(max(data, key=len)))