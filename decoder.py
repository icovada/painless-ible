"Decode files from Ible LedBuild"
import io
from datetime import datetime as dt


def decode_header(infile: io.BufferedReader):
    "Decode file header"

    block = infile.read(16)
    assert block == b'\x50\x48\x54\x00\x00\x00\x00\x00\x31\x31\x30\x00\x00\x00\x00\x00'

    date = infile.read(11)
    day, month, year, _ = date.decode('ascii').split("/")
    begin_date = dt(int(year), int(month), int(day))

    data_length = int.from_bytes(infile.read(4), byteorder='little')

    infile.read(1)
    zeroes = infile.read(16)

    return begin_date, data_length


def decode_timetable(data: io.BytesIO, length: int):
    "Decode timetable section"

    def read_one_slot(data: io.BytesIO) -> io.BytesIO:
        "Read until slot end \x00\x1e"

        def check_eos(data: io.BytesIO) -> bool:
            "Check last two bytes are \x00\x1e"

            data.seek(data.tell()-2)
            return data.read(2) == b'\x00\x1e'

        slot_data = io.BytesIO()
        chunk = slot_data.read(2)
        if len(chunk) == 0:
            return

        slot_data.write(chunk)

        while not check_eos(data):
            data.read(1)

        return slot_data

    def decode_one_slot(data: io.BytesIO):
        "Decode one slot of information"

        number = int.from_bytes(data.read(2), byteorder='little')

        colour = data.read(4)
        colour2 = data.read(4)
        # assert colour2 == colour

        slot_type = data.read(6)

        end_min = int.from_bytes(data.read(1), byteorder='little')
        end_hour = int.from_bytes(data.read(1), byteorder='little')

        start_min = int.from_bytes(data.read(1), byteorder='little')
        start_hour = int.from_bytes(data.read(1), byteorder='little')

        weekday_map = data.read(1)

        end_day = int.from_bytes(data.read(1), byteorder='little')
        end_month = int.from_bytes(data.read(1), byteorder='little')
        end_year = int.from_bytes(data.read(2), byteorder='little')

        start_day = int.from_bytes(data.read(1), byteorder='little')
        start_month = int.from_bytes(data.read(1), byteorder='little')
        start_year = int.from_bytes(data.read(2), byteorder='little')

        program_index = int.from_bytes(data.read(1), byteorder='little')

        unknown = data.read(2)

        return {
            "number": number,
            "colour": colour,
            "colour2": colour2,
            "slot_type": slot_type,
            "end_min": end_min,
            "end_hour": end_hour,
            "start_min": start_min,
            "start_hour": start_hour,
            "start_year": start_year,
            "weekday_map": weekday_map,
            "end_day": end_day,
            "end_month": end_month,
            "end_year": end_year,
            "start_day": start_day,
            "start_month": start_month,
            "program_index": program_index,
            "unknown": unknown,
        }

    all_slots = []
    while section := read_one_slot(data):
        section_bytes = io.BytesIO(section)
        all_slots.append(decode_one_slot(section_bytes))

    return all_slots


def decode_footer(infile: io.BufferedReader):
    "Decode footer"


def decoder(infile):
    "Decoding function"

    begin_date, data_length = decode_header(infile)

    data = io.BytesIO(infile.read(data_length))

    timetable = decode_timetable(data, data_length)

    footer = decode_footer(infile)


def main():
    "Main function"

    with open("calfake.cal", "rb") as infile:
        result = decoder(infile)


if __name__ == '__main__':
    main()
