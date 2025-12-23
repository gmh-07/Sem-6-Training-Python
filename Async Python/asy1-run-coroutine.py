


# Here we had not used await so we cannot wait for 2 seconds and it will directly print GoodBye HelloWorld! after Hello World!

import asyncio


async def main():
    print("Hello World")
    asyncio.sleep(2)
    print("GoodBye HelloWorld")


print("#### Type of the main(): ",type(main()))

print("#### Running coroutine...")
asyncio.run(main())

