from asyncio import new_event_loop, sleep

from sdbus import request_default_bus_name_async

from yaff.messages import YaffInterface

loop = new_event_loop()

export_object = YaffInterface()

async def startup() -> None:
    await request_default_bus_name_async('org.yaff.interface')
    export_object.export_to_dbus('/')


loop.run_until_complete(startup())

loop.run_forever()