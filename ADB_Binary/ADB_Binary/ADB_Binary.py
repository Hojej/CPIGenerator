array_Token = []
array_Length = []
array_CPI = []
file_size = 0

with open("C:\\Users\\hooje\\Downloads\\168.bin", mode="rb") as file:
    file.read(18)
    
    for i in range(131455):
        byte = file.read(24)

        tempArr_Token = []
        tempArr_Length = []
        tempArr_CPI = []

        Token = byte[:4].hex()
        Length = byte[4:8].hex()
        CPI = byte[8:].hex()

        for i in range(4):
            tempArr_Token.append(Token[(i*2):((i*2)+2)])
            tempArr_Length.append(Length[(i*2):((i*2)+2)])

        for i in range(16):
            tempArr_CPI.append(CPI[(i*2):((i*2)+2)])

        array_Token.append(tempArr_Token)
        array_Length.append(tempArr_Length)
        array_CPI.append(tempArr_CPI)


    print(array_Token)
    print("-------------")
    print(array_Length)
    print("-------------")
    print(array_CPI)
    print("-------------")