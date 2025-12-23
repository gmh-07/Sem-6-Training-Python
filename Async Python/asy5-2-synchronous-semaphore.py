
import asyncio

async def access_resource(semaphore,resource_id):
    async with semaphore:
        print('#'*40)
        print(f"{id} : Accessing resource: {resource_id}")
        await asyncio.sleep(3)
        print(f"{id} : Releasing resource : {resource_id}")


async def main():
    semaphore = asyncio.Semaphore(2)   #allow 2 concurrent accesses
    await asyncio.gather(*(access_resource(semaphore,i) for i in range(4))) # unpacking the tuple here


asyncio.run(main())

# sab ek ke baad ek execute ho rahe hai due to they are sharing some resources