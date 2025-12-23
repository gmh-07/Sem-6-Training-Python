
import asyncio

async def fetch_data(delay,id):
    print(f"Fetching data with a delay of {delay} seconds... for ID: {id}.........")
    await asyncio.sleep(delay)
    print(f"Data fetched after {delay} seconds... for ID: {id}.........")
    return f"Data from {delay}  seconds... for ID: {id}........."


async def main():
    print("Start of main coroutine")
    result = await asyncio.gather(
        fetch_data(3,1),
        fetch_data(5,2),
        fetch_data(3,3)
    )

    print(type(result))

    for i,res in enumerate(result):
        print(f"Coroutine {i+1} completed with result : ",res)


asyncio.run(main())




