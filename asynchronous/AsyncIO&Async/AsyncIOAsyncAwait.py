import asyncio

# async def main():
#     print('Fatma')
#     await foo('text')
#     print('finished')


async def main():
    print('Fatma')
    task = asyncio.create_task(foo('text'))
    # await task => wait for the task to be finished before 
    await asyncio.sleep(0.5)
    print('finished')


async def foo(text):
    print(text)
    await asyncio.sleep(10)


# print(main()) => we can't run an async function directly

# await main() => false can't use await outside of the async function

asyncio.run(main())

