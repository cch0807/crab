from functools import wraps


def redis_operation(fn):
    @wraps(fn)
    async def wrapper(self, *args, **kwargs):
        async with self.get_redis_connection() as redis:
            return await fn(self, redis, *args, **kwargs)

    return wrapper
