"Define binary data format as structs"
from struct import pack, unpack
import io
from collections import namedtuple

RECORD_FORMAT = "<xxHHIIxxIBBBBBBBHBBHBxB"
SEC_RECORD_FORMAT = "<xxxHHIIxxIBBBBBBBHBBHBxB"


def ible_encode_animation(
        group: int,
        timeslot: int,
        colour: int,
        end_min: int,
        end_hour: int,
        start_min: int,
        start_hour: int,
        end_day: int,
        end_month: int,
        end_year: int,
        start_day: int,
        start_month: int,
        start_year: int,
        index: int,
        firstrun: bool = True):
    "Generate animation struct"

    data = [
        group,
        timeslot,
        colour,
        colour,
        int.from_bytes(b'\x58\xf7\x31\x00', byteorder='little'),
        end_min,
        end_hour,
        start_min,
        start_hour,
        255,
        end_day,
        end_month,
        end_year,
        start_day,
        start_month,
        start_year,
        index,
        int.from_bytes(b'\x1e', byteorder='little'),
    ]

    if firstrun:
        b_out = pack(RECORD_FORMAT, *data)
    else:
        b_out = pack(SEC_RECORD_FORMAT, *data)

    return b_out


def ible_decode_animation(stream: io.BufferedIOBase) -> dict | None:
    """
    Read struct and return decoded data as dict
    Returns None if animation data block is over
    Does not rewind incoming stream
    """

    Animation = namedtuple("Animation", "group timeslot colour colour2 unknown1 end_min end_hour start_min start_hour day_bitmap end_day end_month end_year start_day start_month start_year index separator")
    data_block = b''

    this_byte = stream.read(1)
    if this_byte == b'\x1d':
        # End of animation blocks
        return None

    data_block += this_byte

    data_block += stream.read(35)
    format = RECORD_FORMAT
    
    if data_block[-2:] != b'\x00\x1e':
        data_block += stream.read(1)
        format = SEC_RECORD_FORMAT

    assert data_block[-2:] == b'\x00\x1e'

    data = Animation._make(unpack(format, data_block))

    return data