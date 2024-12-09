from typing import Coroutine, Any


# === Async
def st_await(coroutine: Coroutine) -> Any:
    """<需要 nest_asyncio> 在Streamlit环境中执行单个异步协程。
    :param coroutine: 要执行的异步协程
    :return Any: 协程的执行结果
    示例:
    async def example():
        await asyncio.sleep(1)
        return "Done"
    result = st_async(example())
    """
    import asyncio
    loop = None
    try:
        loop = asyncio.new_event_loop()
        return loop.run_until_complete(coroutine)
    except Exception as e:
        print(f"st_async 捕获异常 {e=}")
        if loop is not None:
            loop.close()
        loop = asyncio.new_event_loop()
        return loop.run_until_complete(coroutine)
    finally:
        if loop is not None:
            loop.close()


def st_gather(coroutines: list[Coroutine], return_exceptions: bool = False) -> list[Any]:
    """ <需要 nest_asyncio>
    :param return_exceptions: 如果为True，异常将被返回而不是抛出。默认为False。
    :param coroutines: 要执行的协程列表
    :return 所有协程的结果列表。
    注意:
    此函数创建一个新的事件循环来运行协程，适用于在非异步环境（如Streamlit）中运行异步代码。
    示例:
    async def example(x):
        await asyncio.sleep(1)
        return x * 2

    tasks = [example(i) for i in range(3)]
    results = st_async_gather(tasks)  # [0, 2, 4]
    """
    import asyncio

    async def run_coroutines():
        return await asyncio.gather(*coroutines, return_exceptions=return_exceptions)

    return st_await(run_coroutines())
