class Cube_cutting:
    def cube(self, l: int, w: int, h: int, cuts: List[List[int]]):
        removed = set()

        for cut in cuts:
            x1, y1, z1, x2, y2, z2 = cut
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    for z in range(z1, z2+1):
                        removed.add((i, j, z))

        volume = l * w * h
        remaining = volume - len(removed)
        return remaining

if __name__ == "__main__":
    swordsman = Cube_cutting()
    remaining = swordsman.cube(4, 4, 4, [[1, 1, 1, 2, 2, 2]])
    print(remaining)