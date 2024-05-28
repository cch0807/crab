from contextlib import asynccontextmanager

import aioredis
from app.core.config import get_settings
from app.db.session import redis_operation


class RedisClient:
    def __init__(self):
        self.setting = get_settings().redis.model_dump()

    @asynccontextmanager
    async def get_redis_connection(self):
        try:
            redis = await aioredis.Redis(
                **self.setting,
            )
        except ConnectionError as e:
            print(f"Redis connection failure -> { str(e) }")

        try:
            yield redis
        finally:
            await redis.close()

    @redis_operation
    async def health_check(self, redis):
        pong = await redis.ping()
        return pong
