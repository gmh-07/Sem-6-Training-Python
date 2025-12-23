import asyncio

async def fetch_data(delay,id):
    print(f"Fetching data with a delay of {delay} seconds... for ID: {id}.........")
    await asyncio.sleep(delay)
    print(f"Data fetched after {delay} seconds... for ID: {id}.........")
    return f"Data from {delay}  seconds... for ID: {id}........."



# with create task we have executing the coroutines simultaneously pehle just with await ye possible nahi tha
async def main():
    print("Start of main coroutine")
    coroutine1 = asyncio.create_task(fetch_data(3,1))
    coroutine2 = asyncio.create_task(fetch_data(5,2))
    coroutine3 = asyncio.create_task(fetch_data(3,3))
    print("Coroutines are created, now running...")
    result1 = await coroutine1
    print("Coroutine1 completed with result : ","(",result1,")")
    result2 = await coroutine2
    print("Coroutine2 completed with result  : ","(",result2,")")
    result3 = await coroutine3
    print("Coroutine3 completed with result  : ", "(", result3, ")")


asyncio.run(main())




