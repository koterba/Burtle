from burtle import Burtle, BScreen, done
import random
import time

wn = BScreen()
wn.tracer(0, 0)

SIZE = 20
arr = [[1 if random.randint(0, 1) == 1 else 0 for _ in range(40)] for _ in range(40)]

pen = Burtle()
pen.ht()
pen.draw_grid(arr, SIZE, special=(1, "black"))


def gol(lis):
    temp = []

    for j, row in enumerate(lis):
        temp_row = []
        for i, elem in enumerate(row):
            try:
                on_neighbors = (
                        lis[j - 1][i - 1] +
                        lis[j - 1][i] +
                        lis[j - 1][i + 1] +
                        lis[j][i - 1] +
                        lis[j][i + 1] +
                        lis[j + 1][i - 1] +
                        lis[j + 1][i] +
                        lis[j + 1][i + 1]
                        )

                # logic
                if lis[j][i] == 1:
                    if on_neighbors == 2 or on_neighbors == 3:  # if on, 3or2 alive near, keep on
                        temp_row.append(1)
                        continue
                    temp_row.append(0)  # if on but less than 2 or more than 3, kill
                    continue
                if on_neighbors == 3:
                    temp_row.append(1)
                    continue
                temp_row.append(0)

            except:
                temp_row.append(lis[j][i])

        temp.append(temp_row)

    return temp


for _ in range(100):
    pen.clear()
    arr = gol(arr)
    pen.draw_grid(arr, SIZE, special=(1, "black"))
    wn.update()

wn.update()
done()
