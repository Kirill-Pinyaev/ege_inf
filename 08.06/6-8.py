from functools import lru_cache


def move(h):
    a, b = h
    return (a + 2, b), (a, b + 2), (a * 3, b), (a, b * 3)


@lru_cache(None)
def game(h):
    if sum(h) >= 113:
        return 'W'
    if any(game(m) == 'W' for m in move(h)):
        return 'P1'
    if all(game(m) == 'P1' for m in move(h)):
        return 'B1'
    if any(game(m) == 'B1' for m in move(h)):
        return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in move(h)):
        return 'B2'


for s in range(1, 101):
    if game((11, s)) is not None:
        print(s, game((11, s)))