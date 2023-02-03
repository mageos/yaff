from sdbus import (DbusInterfaceCommonAsync, dbus_method_async, dbus_property_async, dbus_signal_async)

class YaffInterface(
    DbusInterfaceCommonAsync,
    interface_name='org.yaff.interface'
):
    @dbus_method_async(input_signature='s', result_signature='s')
    async def echo(self, i: str) -> str:
        return i
