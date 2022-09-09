import asyncio
import inspect


def is_async(callable_unit):
    is_async_gen = inspect.isasyncgenfunction(callable_unit)
    is_coro_fn = asyncio.iscoroutinefunction(callable_unit)
    return is_async_gen or is_coro_fn
