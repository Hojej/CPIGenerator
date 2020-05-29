from binascii import unhexlify
import codecs

padding = 8
with open('Failed.bin', 'wb') as file:
    start = "\x00\x00\x55\x55\x55\x55\x55\x55\x55\x55"
    chirpStart = "\x00\x00\x83\x83\x83\x83\x83\x83\x83\x83"
    chirpToken = "\x6a\x0f\x00\x00"
    chirpLength = "00000000"
    startFlag = True
    lengthFlag = True
    count = 0
    length = 0

    while(count < 512):
        toSave = ""
        if(startFlag):
            print(chirpLength)
            toSave = start + chirpToken + str(unhexlify(chirpLength))
            startFlag = False
        else:
            print(chirpLength)
            toSave = chirpStart + chirpToken + str(unhexlify(chirpLength))

        print(toSave)
        file.write(toSave.encode())
        if(length > 0xFFFF00):
            length -= 0xFFFF00

        chirpLength = '{0:0{1}X}'.format(length,8)
        print("%d: Byte Counter: %s" % (count+1, chirpLength))
        count += 1
        length += 0x180000