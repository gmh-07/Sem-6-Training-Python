# Here we will wait for 2 seconds

import asyncio

async def fetch_data(delay,id):
    print(f"Fetching data with a delay of {delay} seconds... for ID: {id}.........")
    await asyncio.sleep(delay)
    # if id==2:
    #     raise ValueError(f"An Error occured for {id}")
    print(f"Data fetched after {delay} seconds... for ID: {id}.........")
    return f"Data from {delay}  seconds... for ID: {id}........."


async def main():
    print("Start of main coroutine")
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i,sleep_time in enumerate([3,5,3],start=1):
            task = tg.create_task(fetch_data(sleep_time,i))
            tasks.append(task)

    for i,task in enumerate(tasks):
        print(f"Coroutine {i+1} completed with result : ",task.result())

asyncio.run(main())




