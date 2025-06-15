import asyncio

async def main():

    queue = asyncio.Queue()
    seed_urls = (
        'https://news.ycombinator.com/',
        'https://httpbin.org/delay/2',
        'https://example.com/',
        'https://httpbin.org/delay/3',
        'https://python.org/',
    )
    for url in seed_urls:
        queue.put_nowait(url)

    # Step 3: Concurrency Control with Semaphore
    sem = asyncio.Semaphore(3)  # limit to 3 concurrent fetches

    # Spawn worker tasks
    workers = [asyncio.create_task(worker(f"worker-{i}", queue, sem)) for i in range(5)]
    await asyncio.gather(*workers)


# Worker definition demonstrating semaphore usage
async def worker(name: str, queue: asyncio.Queue, sem: asyncio.Semaphore):
    while not queue.empty():
        url = await queue.get()
        # acquire semaphore before fetching
        #  to limit the number of coroutines that can enter a particular block of code at the same time. 
        async with sem:
            # critical section
            print(f"{name} fetching {url}")
            # placeholder for actual fetch logic
            await asyncio.sleep(1)
        queue.task_done()


if __name__ == "__main__":
    asyncio.run(main())
