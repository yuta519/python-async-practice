import asyncio


async def fetch_data():
    print("Start fetching")
    await asyncio.sleep(2)  # Simulating an I/O operation
    print("Done fetching")
    return {'data': 1}


async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    print('tasks1 and 2 created, but not yet executed')

    value = await task1
    await task2
    print(value)


asyncio.run(main())
