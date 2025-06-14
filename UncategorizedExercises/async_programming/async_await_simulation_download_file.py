import asyncio

async def download_file(filename, delay):
    print(f"Start downloading {filename}...")
    await asyncio.sleep(delay)  # Simulates network delay
    print(f"Finished downloading {filename} after {delay} seconds.")

async def main():
    # Schedule multiple downloads at once
    task1 = download_file("file1.txt", 2)
    task2 = download_file("file2.txt", 3)
    task3 = download_file("file3.txt", 1)

    await asyncio.gather(task1, task2, task3)

# Run the async program
asyncio.run(main())