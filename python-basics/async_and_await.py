"""
async_and_await.py

This file explains asynchronous programming in Python.
Used heavily in backend frameworks like FastAPI.
"""

import asyncio
import time


# ------------------------
# Synchronous example
# ------------------------

def sync_task(name, delay):
    print(f"Start sync task: {name}")
    time.sleep(delay)
    print(f"End sync task: {name}")


def run_sync_tasks():
    start = time.time()

    sync_task("Task 1", 2)
    sync_task("Task 2", 2)

    end = time.time()
    print(f"Sync execution time: {end - start:.2f} seconds")


# ------------------------
# Asynchronous example
# ------------------------

async def async_task(name, delay):
    print(f"Start async task: {name}")
    await asyncio.sleep(delay)
    print(f"End async task: {name}")


async def run_async_tasks():
    start = time.time()

    await asyncio.gather(
        async_task("Task 1", 2),
        async_task("Task 2", 2),
    )

    end = time.time()
    print(f"Async execution time: {end - start:.2f} seconds")


# ------------------------
# Entry point
# ------------------------

if __name__ == "__main__":
    print("\n--- Running synchronous tasks ---")
    run_sync_tasks()

    print("\n--- Running asynchronous tasks ---")
    asyncio.run(run_async_tasks())
