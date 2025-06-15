import asyncio

async def fetch(url: str, sem: asyncio.Semaphore):
    # Step 3 & 4: Concurrency throttle + per-request timeout
    async with sem:
        try:
            # simulate network delay; replace with real fetch if desired
            await asyncio.wait_for(asyncio.sleep(1), timeout=1.5)
            return url, 'OK'
        except asyncio.TimeoutError:
            return url, 'TIMEOUT'

async def main():
    # Step 1 & 2: Entry point & target list
    urls = [
        'https://example.com/',
        'https://httpbin.org/delay/2',
        'https://httpbin.org/status/404',
        'https://python.org/'
    ]

    sem = asyncio.Semaphore(2)  # limit to 2 concurrent fetches
    tasks = [asyncio.create_task(fetch(u, sem)) for u in urls]

    # Step 5: Gather with global timeout and cancellation
    try:
        results = await asyncio.wait_for(
            asyncio.gather(*tasks),
            timeout=3
        )
    except asyncio.TimeoutError:
        print('Overall check took too long; cancelling remaining tasks...')
        for t in tasks:
            t.cancel()
        results = await asyncio.gather(*tasks, return_exceptions=True)

    for url, status in results:
        # handle CancelledError exceptions
        if isinstance(status, Exception):
            print(f'{url} -> CANCELLED')
        else:
            print(f'{url} -> {status}')

if __name__ == '__main__':
    asyncio.run(main())
