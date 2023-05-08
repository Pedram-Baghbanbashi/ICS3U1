iphone_12 = 20
iphone_13 = 15 
iphone_14 = 15

iphone_12_time = 2.13333333333
iphone_13_time = 2.5
iphone_14_time = 2.3

S23_ultra = 15
s23 = 25
s22 = 25
zfold4 = 25
zflip4 = 25

S23_ultra_time = 2.3
s23_time = 1
s22_time = 1
zfold4_time = 1.33333333333
zflip4_time = 1.33333333333

lenovo_thinkpad = 65
Desktop_computer_high_usage = 150
Desktop_computer_low_usage = 80


# Tara - part of device selection
# Pedram - calculations, message, and all other sections

device_list = "device list: iphone 12, iphone 13, iphone 14, S23 ultra, S23, S22, zfold4, zflip4 lenovo thinkpad, Desktop computer high usage (150w) Desktop computer low usage (80w) (Plese type divice name exactly as listed)."

print(device_list)

model = input("what model phone do you want to calculate?")   

if model=="iphone 12":
 use= float(input("How long do you use this device on average per day in hours?"))
    
 if use <= 11:
    time = iphone_12 * iphone_12_time 
    kwh = time / 1000
    total = kwh * 10.45
    weekly_total = total * 7
    weekly_power = kwh * 7
 elif use <= 21:
    time = iphone_12 * iphone_12_time * 2 
    kwh = time / 1000
    total = kwh * 10.45
    weekly_total = total * 7
    weekly_power = kwh * 7
 else:
    time = iphone_12 * iphone_12_time * 3
    kwh = time / 1000
    total = kwh * 10.45
    weekly_total = total * 7
    weekly_power = kwh * 7
 print(f"the daily cost in cents for the iphone 12 is {total}, the aproximate weekly cost would be {weekly_total}, the amount of power used daily is {kwh}kwh, and the aproximate amount of power used weekly is {weekly_power}kwh.")
    

if model=="iphone 13":
 use = float(input("How long do you use this device on average per day in hours?"))

 if use <= 15:
    time = iphone_13 * iphone_13_time 
    kwh = time / 1000
    total = kwh * 10.45
    weekly_total = total * 7
    weekly_power = kwh * 7 
 else:
    time = iphone_13 * iphone_13_time * 2
    kwh = time / 1000
    total = kwh * 10.45
    weekly_total = total * 7
    weekly_power = kwh * 7
 print(f"the daily cost in cents for the iphone 13 is {total}, the aproximate weekly cost would be {weekly_total}, the amount of power used daily is {kwh}kwh, and the aproximate amount of power used weekly is {weekly_power}.kwh")


if model=="iphone 14":
 use = float(input("How long do you use this device on average per day in hours?"))

 if use <= 24.5:
    time = iphone_14 * iphone_14_time 
    kwh = time / 1000
    total = kwh * 10.45
    weekly_total = total * 7
    weekly_power = kwh * 7
 print(f"the daily cost in cents for the iphone 14 is {total}, the aproximate weekly cost would be {weekly_total}, the amount of power used daily is {kwh}kwh, and the aproximate amount of power used weekly is {weekly_power}kwh.")

if model == "S22":
 use = float(input("How long do you use this device on average per day in hours?"))
 if use <= 22:
    time = s22 * s22_time 
    kwh = time / 1000
    total = kwh * 10.45
    weekly_total = total * 7
    weekly_power = kwh * 7
 else:
    time = s22  * s22_time * 2
    kwh = time / 1000
    total = kwh * 10.45
    weekly_total = total * 7
    weekly_power = kwh * 7
 print(f"the daily cost in cents for the s22 is {total}, the aproximate weekly cost would be {weekly_total}, the amount of power used daily is {kwh}kwh, and the aproximate amount of power used weekly is {weekly_power}kwh.") 


if model == "S23_ultra":
 use = float(input("How long do you use this device on average per day in hours?"))
 if use <= 26:
    time = S23_ultra * S23_ultra_time 
    kwh = time / 1000
    total = kwh * 10.45
    weekly_total = total * 7
    weekly_power = kwh * 7
 print(f"the daily cost in cents for the S23 ultra is {total}, the aproximate weekly cost would be {weekly_total}, the amount of power used daily is {kwh}kwh, and the aproximate amount of power used weekly is {weekly_power}kwh.")
    

if model == "S23":
 use = float(input("How long do you use this device on average per day in hours?"))
 if use <= 22:
    time = s23 * s23_time 
    kwh = time / 1000
    total = kwh * 10.45
    weekly_total = total * 7
    weekly_power = kwh * 7
 else:
    time = s23  * s23_time * 2
    kwh = time / 1000
    total = kwh * 10.45
    weekly_total = total * 7
    weekly_power = kwh * 7
 print(f"the daily cost in cents for the s23 is {total}, the aproximate weekly cost would be {weekly_total}, the amount of power used daily is {kwh}kwh, and the aproximate amount of power used weekly is {weekly_power}kwh.")


if model == "zfold4":
 use = float(input("How long do you use this device on average per day in hours?"))

 if use <= 12.716667:
    time = zfold4 * zfold4_time 
    kwh = time / 1000
    total = kwh * 10.45
    weekly_total = total * 7
    weekly_power = kwh * 7
 elif use <= 25.433334:
    time = zfold4 * zfold4_time * 2 
    kwh = time / 1000
    total = kwh * 10.45
    weekly_total = total * 7
    weekly_power = kwh * 7
 print(f"the daily cost in cents for the zfold4 is {total}, the aproximate weekly cost would be {weekly_total}, the amount of power used daily is {kwh}kwh, and the aproximate amount of power used weekly is {weekly_power}kwh.")


if model=="zflip4":
 use = float(input("How long do you use this device on average per day in hours?"))

 if use <= 9.2:
    time = zflip4 * zflip4_time 
    kwh = time / 1000
    total = kwh * 10.45
    weekly_total = total * 7
    weekly_power = kwh * 7
 elif use <= 18.4:
    time = zflip4 * zflip4_time * 2 
    kwh = time / 1000
    total = kwh * 10.45
    weekly_total = total * 7
    weekly_power = kwh * 7
 else:
    time = zflip4  * zflip4_time * 3
    kwh = time / 1000
    total = kwh * 10.45
    weekly_total = total * 7
    weekly_power = kwh * 7
 print(f"the daily cost in cents for the zflip4 is {total}, the aproximate weekly cost would be {weekly_total}, the amount of power used daily is {kwh}kwh, and the aproximate amount of power used weekly is {weekly_power}kwh.")


device = input("What device do you want to calculate?")

if device == "lenovo thinkpad":
    
 pc_use = float(input("How long do you have this device pluged in on average per day in hours?"))
    
 time = lenovo_thinkpad * pc_use
 kwh = time / 1000
 total = kwh * 10.45
 weekly_total = total * 7
 weekly_power = kwh * 7
 print(f"the daily cost in cents for lenovo thinkpad is {total}, the aproximate weekly cost would be {weekly_total}, the amount of power used daily is {kwh}kwh, and the aproximate amount of power used weekly is {weekly_power}kwh.")


if device == "Desktop computer high usage":
    
 pc_use = float(input("How long do you have this device pluged in on average per day in hours?"))

 time = Desktop_computer_high_usage * pc_use
 kwh = time / 1000
 total = kwh * 10.45
 weekly_total = total * 7
 weekly_power = kwh * 7
 print(f"the daily cost in cents for the Desktop computer high usage  is {total}, the aproximate weekly cost would be {weekly_total}, the amount of power used daily is {kwh}kwh, and the aproximate amount of power used weekly is {weekly_power}kwh.")


if device == "Desktop computer low usage":
    
 pc_use = float(input("How long do you have this device pluged in on average per day in hours?"))

 time = Desktop_computer_low_usage  * pc_use
 kwh = time / 1000
 total = kwh * 10.45
 weekly_total = total * 7
 weekly_power = kwh * 7
 print(f"the daily cost in cents for the Desktop computer low usage  is {total}, the aproximate weekly cost would be {weekly_total}, the amount of power used daily is {kwh}kwh, and the aproximate amount of power used weekly is {weekly_power}kwh.")
