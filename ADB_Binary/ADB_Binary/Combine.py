from binascii import unhexlify
import codecs
import time
import socket
import os
import gc

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1.0)
addr = ("127.0.0.1", 4000)
loopCount = 0
padding = 8
while(loopCount < 250):
    loopCount += 1
    print(loopCount)
    with open('TestB.bin', 'wb') as file:
        start = "\x00\x00\x55\x55\x55\x55\x55\x55\x55\x55"
        chirpStart = "\x00\x00\x83\x83\x83\x83\x83\x83\x83\x83"
        chirpToken = "\x6a\x0f\x00\x00"
        chirpToken2 = "\x19\x09\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"
        chirpLength = "00000000"
        startFlag = True
        lengthFlag = True
        count = 0
        length = 0

        while(count < 512):
            toSave = ""
            if(startFlag):
                # print(chirpLength)
                toSave = start + chirpToken + \
                    str(unhexlify(chirpLength).decode("ISO-8859-1"))
                startFlag = False
            else:
                # print(chirpLength)
                toSave = chirpStart + chirpToken + \
                    str(unhexlify(chirpLength).decode("ISO-8859-1"))

            if(count < 101):
		#if(count == 0):
		#    for i in range(256):
                #        toSave = toSave + "\x0A\x0A\x0A\x0A"
                #        toSave = toSave + "\xFF\xFF\xFF\xFF"
                #        for a in range(4):
                #            toSave = toSave + "\x0A"
                #            toSave = toSave + "\x0A"
                #            toSave = toSave + "\x00"
                #            toSave = toSave + "\x0A"
                if(count < 51):
                    for i in range(256):
                        toSave = toSave + "\x0A\x0A\x0A\x0A"
                        toSave = toSave + "\xFF\xFF\xFF\xFF"
                        for a in range(4):
                            toSave = toSave + "\x0A"
                            toSave = toSave + "\x0A"
                            toSave = toSave + "\x00"
                            toSave = toSave + "\x0A"
                else:
                    for i in range(256):
                        toSave = toSave + "\x0A\x0A\x0A\x0A"
                        toSave = toSave + "\x0A\x0A\x0A\x0A"
                        for a in range(4):
                            toSave = toSave + "\x00"
                            toSave = toSave + "\x00"
                            toSave = toSave + "\x00"
                            toSave = toSave + "\x0A"
            elif(count < 201):
                for i in range(256):
                    toSave = toSave + "\x0A\x0A\x0A\x0A"
                    toSave = toSave + "\x0A\x0A\x0A\x0A"
                    for a in range(4):
                        toSave = toSave + "\x0A"
                        toSave = toSave + "\x00"
                        toSave = toSave + "\x0A"
                        toSave = toSave + "\x0B"
            elif(count < 301):
                for i in range(256):
                    toSave = toSave + "\x0A\x0A\x0A\x0A"
                    toSave = toSave + "\x0A\x0A\x0A\x0A"
                    for a in range(4):
                        toSave = toSave + "\x00"
                        toSave = toSave + "\x0A"
                        toSave = toSave + "\x00"
                        toSave = toSave + "\x0C"
            elif(count < 401):
                for i in range(256):
                    toSave = toSave + "\x00\x00\x00\x00"
                    toSave = toSave + "\x00\x00\x00\x00"
                    for a in range(4):
                        toSave = toSave + "\x00"
                        toSave = toSave + "\x0A"
                        toSave = toSave + "\x00"
                        toSave = toSave + "\x0C"
            else:
                for i in range(256):
                    toSave = toSave + "\x00\x00\x00\x00"
                    toSave = toSave + "\x00\x00\x00\x00"
                    for a in range(4):
                        toSave = toSave + "\xFF"
                        toSave = toSave + "\xFF"
                        toSave = toSave + "\xFF"
                        toSave = toSave + "\xFF"

            # print(toSave.encode())
            file.write(toSave.encode("ISO-8859-1"))
            if(length > 0xFFFF00):
                length -= 0xFFFF00

            chirpLength = '{0:0{1}X}'.format(length, 8)
            #print("%d: Byte Counter: %s" % (count+1, chirpLength))
            count += 1
            length += 0x180000

            #file_name = "/home/ubuntu/workspace/CPISender/CPISender/CPISender/TestB.bin"
    with open("TestB.bin", "rb") as f:
        data = f.read(6162)
        #data, server = client_socket.recvfrom(1024)
        while(data):
            if(client_socket.sendto(data, addr)):
                data = f.read(6162)
                # print("Sending..")
                count = count + 1
    gc.collect()
    print("Check diff")
    os.system("diff TestB.bin OldTestB.bin")
    print("Rename")
    os.rename('TestB.bin', 'OldTestB.bin')
    # time.sleep(0.05)
client_socket.close()
f.close()
print("Closing")