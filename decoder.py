"Decode files from Ible LedBuild"
import io
from datetime import datetime as dt
from iblestructs import ible_decode_animation


def decode_header(infile: io.BufferedReader):
    "Decode file header"

    block = infile.read(16)
    assert block == b'\x50\x48\x54\x00\x00\x00\x00\x00\x31\x31\x30\x00\x00\x00\x00\x00'

    date = infile.read(11)
    day, month, year, _ = date.decode('ascii').split("/")
    begin_date = dt(int(year), int(month), int(day))

    data_length = int.from_bytes(infile.read(4), byteorder='little')

    infile.read(1)

    return begin_date, data_length


def decode_footer(infile: io.BufferedReader):
    "Decode footer"

    footer_data = b''

    while True:
        footer_data += infile.read(1)
        if footer_data[-3:] == b'\x1c\x1d\x01':
            break

    program_list = footer_data.split(b'\x1c')
    program_strings = [str(x) for x in program_list]
    return program_strings

def decoder(infile):
    "Decoding function"

    begin_date, data_length = decode_header(infile)

    # data = io.BytesIO(infile.read(data_length))
    # timetable = decode_timetable(data, data_length)

    animations = []
    while (animation := ible_decode_animation(infile)) is not None:
        animations.append(animation)

    footer = decode_footer(infile)

    return True


def main():
    "Main function"

    with open("calfake.cal", "rb") as infile:
        result = decoder(infile)


if __name__ == '__main__':
    main()
