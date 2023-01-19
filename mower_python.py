import serial;
import matplotlib.pyplot as plt
portnumber = "COM4"
baudrate = 9600
ser = serial.Serial(portnumber,baudrate)
while True:
    data = str(ser.readline())
    data = data.rstrip()
    data = data.replace("","")#bruh add the strings
    data = data.replace("","")#bruh add the strings
    data = data.replace("","")#bruh add the strings
    #split by the comma
    data = data.split(",")
    px = float(data[0])
    py = float(data[1])
    theta =  float(data[2])
    print(px)
    print(py)
    print(theta)
    print(data)
    #print(len(data))
    plt.plot(px,py,"o", "red")
    plt.show()
