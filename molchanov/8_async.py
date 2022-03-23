import requests
from time import time
import asyncio
import aiohttp


def time_performance(func):
    def inner(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        delta = end_time - start_time
        print(func.__name__, 'run time', delta)
        return result
    return inner


def get_file(url):
    r = requests.get(url, allow_redirects=True)
    return r


def write_file(response):
    filename = response.url.split('/')[-1]
    with open(filename, 'wb') as file:
        file.write(response.content)


@time_performance
def main(url):
    for i in range(10):
        write_file(get_file(url))


def write_image(data):
    filename = 'file-{}.jpeg'.format(int(time() * 1000))
    with open(filename, 'wb') as file:
        file.write(data)


async def fetch_content(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_image(data)


@time_performance
async def main2(url):
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(fetch_content(url, session))
            tasks.append(task)
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    url = 'https://loremflickr.com/320/240'
    # main(url)
    asyncio.run(main2(url))
