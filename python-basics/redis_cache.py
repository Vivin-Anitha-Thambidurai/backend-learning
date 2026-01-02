"""
redis_cache.py

Demonstrates Redis caching with FastAPI.
Used for performance optimization in production backends.
"""

from fastapi import FastAPI
import redis
import time
import json

app = FastAPI(title="Redis Cache Example")

# ------------------------
# Redis connection
# ------------------------

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True
)

CACHE_EXPIRE_SECONDS = 30


# ------------------------
# Routes
# ------------------------

@app.get("/")
def root():
    return {"message": "Redis caching enabled 🚀"}


@app.get("/expensive-data")
def expensive_data():
    cache_key = "expensive_data"

    # Try cache
    cached = redis_client.get(cache_key)
    if cached:
        return {
            "source": "redis_cache",
            "data": json.loads(cached)
        }

    # Simulate slow computation
    time.sleep(5)
    data = {
        "value": "This data took 5 seconds to compute"
    }

    # Save to Redis
    redis_client.setex(
        cache_key,
        CACHE_EXPIRE_SECONDS,
        json.dumps(data)
    )

    return {
        "source": "generated",
        "data": data
    }


@app.delete("/cache")
def clear_cache():
    redis_client.delete("expensive_data")
    return {"message": "Cache cleared"}
