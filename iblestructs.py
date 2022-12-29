"Define binary data format as structs"
from struct import pack

RECORD_FORMAT = "<xxHHIIxxIBBBBBBBHBBHBxB"
SEC_RECORD_FORMAT = "<xxxHHIIxxIBBBBBBBHBBHBxB"


def ible_encode(
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
