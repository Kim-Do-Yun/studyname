OnOff = False
Volumn = 10
channel = 5

def power():
    global OnOff
    
    if OnOff == False :
        OnOff = True
        print("| 전원을 켰습니다. |")
    else :
        OnOff = False
        print("| 전원을 껐습니다. |")

def setVolumnUp(size):
    global OnOff, Volumn

    if OnOff == False :
        print("TV가 꺼져있습니다.")
    else:
        Volumn += size

        if Volumn > 20:
            Volumn = 20

def setVolumnDown(size):
    global OnOff, Volumn

    if OnOff == False :
        print("TV가 꺼져있습니다.")
    else:
        Volumn += size

        if Volumn < 0:
            Volumn = 1

def setChannelUp(size):
    global OnOff, channel

    if OnOff == False :
        print("TV가 꺼져있습니다.")
    else:
        channel += size

        if chaanel > 10:
            channel = 10

def setChannelDown(size):
    global OnOff, channel

    if OnOff == False :
        print("TV가 꺼져있습니다.")
    else:
        channel += size

        if chaanel < 0:
            channel = 1

def getNow():
    print(OnOff, Volumn, channel)

while True:
    print("========================================")
    print("1. 전원 끄기\n 2. 전원 켜기\n 3. 볼륨 조절\n 4. 채널 조절\n 5. 현재의 상태 출력\n 6. 프로그램 종료\n")
    print("========================================")
    print("원하는 기능의 번호를 입력하세요", end=" ")
    a = int(input( ))
    if ((a == 1) or (a == 2)):
        power()
    elif a == 3:
        setVolumnUp(size)
        setVolumnDown(size)
    elif a == 4:
        setChannelUp(size)
        setChannelDown(size)
    elif a == 5:
        getNow()
    elif a == 6:
        break



