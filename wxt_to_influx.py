import asyncio

def wxt_line_to_influx_line(wxt_line):
    influx_line_parts = ['wxt_artjarvi']

    parts= wxt_line.strip().split(',')[1:]

    if not parts:
        return None
    
    for part in parts:
        meas = part[0][0:2]
        value = float(part[3:-1])
        influx_line_parts.append(f'{meas}={value}')
    return (' '.join(influx_line_parts))

async def wxt_client(password):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 2011)

    influx_reader, influx_writer = await asyncio.open_connection(
        '127.0.0.1', 8083)                                         
    
    writer.write(password.encode() + b'\r\n')
    await writer.drain()

    while True:
        data = await reader.read(255)
        print(f'Received: {data.decode()!r}')

        influx_line = wxt_line_to_influx_line(data.decode('ascii'))
        print(f'To influx: {influx_line}')
        influx_writer.write((influx_line+'\n').encode('ascii'))
        #await influx_writer.drain()

    print('Close the connection')
    writer.close()
    #await writer.wait_closed()

loop=asyncio.get_event_loop()
loop.run_until_complete(wxt_client('password'))







