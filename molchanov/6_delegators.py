

def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


class CustomException(Exception):
    pass


def sub_get():
    while True:
        try:
            message = yield
        except CustomException:
            print('CustomException')
            break
        except StopIteration:
            print('StopIteration')
            break

        else:
            print('.......', message)
    return 'returned from sub_gen()'


@coroutine
def delegator(g):
    result = yield from g
    print(result)
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except CustomException as e:
    #         g.throw(e)


sg = sub_get()
g = delegator(sg)
g.send('ok')
# g.throw(CustomException)
g.throw(StopIteration)
