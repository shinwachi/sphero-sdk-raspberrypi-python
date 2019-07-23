import sys
import asyncio

from sphero_sdk import AsyncSpheroRvr
from sphero_sdk import SerialAsyncDal

loop = asyncio.get_event_loop()

rvr = AsyncSpheroRvr(
    dal = SerialAsyncDal(
        loop
    )
)

async def get_main_app_version():
    major, minor, build = await rvr.get_main_application_version(target = 1, timeout = 5)
    print('{} {}.{}.{}'.format("Nordic", major, minor, build))

    major, minor, build = await rvr.get_main_application_version(target = 2, timeout = 5)
    print('{} {}.{}.{}'.format("ST", major, minor, build))


loop.run_until_complete(
    asyncio.gather(
        get_main_app_version()
    )
)

loop.stop()
loop.close()
