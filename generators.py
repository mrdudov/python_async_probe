

def simbol_generator(srting: str) -> str:
    for i in srting:
        yield i


def num_generator(n):
    for i in range(n):
        yield i

g1 = simbol_generator('example')
g2 = num_generator(7)

tasks = [g1, g2]

while tasks:
    task = tasks.pop(0)
    try:
        j = next(task)
        print(j)
        tasks.append(task)
    except StopIteration:
        pass
