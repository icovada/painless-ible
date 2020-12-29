# painless-ible
Because he default LedBulder calendar sucks for me


## The original application
The application (LedBuild) allows to program animations and text for LED panels built by the now foreclosed IBLE Srl. This project only takes in consideration their Pharnacy Cross

The configuration consists of a list of many preset animations called "programs" and customisable scrolling text.

You must define a "base" animation which will be used when no overrides are set

### Scheduling animations

The application provides a calendar window with two levels of nested settings

* "Colour": a set of up to 6 timeslots
* Timeslot: Can go from midnight (00:00) to midnight (24:00). Every timeslot can contain different lists of programs (animations)

Every day of the year can be assigned to a different "colour".

## Savefile dissection

Schedules are output as a binary .cal file and contain 12 solar months of data.

This is the sample content of one schedule called "APERTOoradata" set on the 1st of January 2021 from 00:00 to 24:00

```
00000000: 5048 5400 0000 0000 3131 3000 0000 0000  PHT.....110.....
00000010: 312f 312f 3230 3231 2f00 0045 0000 001d  1/1/2021/..E....
00000020: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000030: 999a 5300 0018 0000 2001 01e5 0701 01e5  ..S..... .......
00000040: 0700 001e 1d41 5045 5254 4f6f 7261 6461  .....APERTOorada
00000050: 7461 1c1d 00ff 001d                      ta......
```

Let's dissect the binary code:

### File header
* Header: `5048 5400 0000 0000 3131 3000 0000 0000  PHT.....110.....`
* Beginning date of schedule. `String(11)`, right-padded with zeroes `312f 312f 3230 3231 2f00 00 1/1/2021/..`
* Length of file. `Long`, little endian `45 0000 00 E...`
* Separator `1D`
* Padding: 16 bytes of zeroes

### File footer (begins at 44)
* Separator `1D`
* `1C`-separated list of program names, `String`: `41 5045 5254 4f6f 7261 6461 7461 1c .....APERTOoradata.`
* Separator `1D`
* Unknown `00 FF 00`
* Separator `1D`

### Program (animation) data
* Start of block: `999a 5300`
* End time, minutes, `int` `00`
* End time, hours, `int` `18`
* Start time, minutes, `int` `00`
* Start time, hours, `int` `00`
* Unknown `2001 01e5 0701 01e5 0700 00`
* Field separator: `1e 1d`
* Program name, `String()
