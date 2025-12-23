# Here we will wait for 2 seconds

import asyncio

async def fetch_data(delay,id):
    print(f"Fetching data with a delay of {delay} seconds... for ID: {id}.........")
    await asyncio.sleep(delay)
    if id==2:
        raise ValueError(f"An Error occured for {id}")
    print(f"Data fetched after {delay} seconds... for ID: {id}.........")
    return f"Data from {delay}  seconds... for ID: {id}........."


async def main():
    print("Start of main coroutine")
    coroutine1 = asyncio.create_task(fetch_data(2, 1))
    coroutine2 = asyncio.create_task(fetch_data(10, 2))
    coroutine3 = asyncio.create_task(fetch_data(2, 3))
    print("Coroutines are created, now running...")
    result1 = await coroutine1
    print("Coroutine1 completed with result : ", "(", result1, ")")
    result2 = await coroutine2
    print("Coroutine2 completed with result  : ", "(", result2, ")")
    result3 = await coroutine3
    print("Coroutine3 completed with result  : ", "(", result3, ")")

asyncio.run(main())




