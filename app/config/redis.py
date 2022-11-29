import aioredis
from common import env


redis = aioredis.from_url(url=env.REDIS_URL) 