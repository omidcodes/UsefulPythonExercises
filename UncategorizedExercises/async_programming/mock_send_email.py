import asyncio

async def send_email(email_address, delay):
    print(f"Sending email to {email_address}")
    await asyncio.sleep(delay)
    print(f"Email sent to {email_address} after {delay} seconds.")


async def main():

    emails = [
        ("a@gmail.com", 2),
        ("b@gmail.com", 4),
        ("c@gmail.com", 1),
        ("d@gmail.com", 3),
    ]


    tasks = []
    for email, delay in emails:
        tasks.append(send_email(email, delay))

    await asyncio.gather(*tasks)


asyncio.run(main())
