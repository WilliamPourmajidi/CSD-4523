import asyncio
import threading

async def async_task():
    await asyncio.sleep(1)
    print("Async Task")

def thread_task(loop):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(async_task())

loop = asyncio.new_event_loop()
thread = threading.Thread(target=thread_task, args=(loop,))
thread.start()
thread.join()
