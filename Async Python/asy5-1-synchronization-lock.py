
import asyncio

shared_resource = 0

lock = asyncio.Lock()

async def modify_shared_resource(id):
    global shared_resource
    async with lock:
        print('#'*40)
        print(f"{id} : Resource before modification: {shared_resource}")
        shared_resource += 1
        await asyncio.sleep(3)
        print(f"{id} : Resource after modification : {shared_resource}")


async def main():
    await asyncio.gather(*(modify_shared_resource(i+1) for i in range(4))) # unpacking the tuple here


asyncio.run(main())

# sab ek ke baad ek execute ho rahe hai due to they are sharing some resources