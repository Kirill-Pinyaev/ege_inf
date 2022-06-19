from functools import lru_cache


def move(h):
    a = h
    return (a + 3), (a * 2)


@lru_cache(None)
def game(h):
    if h >= 33:
        return 'W'
    if any(game(m) == 'W' for m in move(h)):
        return 'P1'
    if all(game(m) == 'P1' for m in move(h)):
        return 'B1'
    if any(game(m) == 'B1' for m in move(h)):
        return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in move(h)):
        return 'B2'
for s in range(1, 32):
    if game(s) is not None:
        print(s, game(s))