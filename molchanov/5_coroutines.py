

def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


def sub_gen():
    x = 'ready to accept message'
    message = yield x
    print('sub_gen received:', message)


@coroutine
def average():
    count = 0
    total = 0
    result = None

    while True:
        try:
            x = yield result
        except StopIteration:
            print('Done')
            break
        else:
            count += 1
            total += x
            result = round(total / count, 2)
    return result


gen = average()
# gen.send(None)
print(gen.send(4))
print(gen.send(5))
print(gen.send(7))
print(gen.send(10))

try:
    gen.throw(StopIteration)
except StopIteration as e:
    print('Average:', e.value)


# print(gen.throw(StopIteration))
