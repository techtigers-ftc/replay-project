from machine import Pin, ADC
from time import sleep

thresholds = (1400, 1100, 220, 220)
#TODO: Figure out thresholds, test by screening
def read():
    
    for inp in inputs:
        inp.atten(ADC.ATTN_0DB)
      
    ref_1 = read_pressure(outputs, inputs)
    sleep(0.1)
    ref_2 = read_pressure(outputs, inputs)
    sleep(0.1)        
    ref_3 = read_pressure(outputs, inputs)
    sleep(0.1)
    ref_4 = read_pressure(outputs, inputs)
    sleep(0.1)        
    ref_5 = read_pressure(outputs, inputs)
    ref_avg = []
    for sensor in range(0, 4):
        ref_sum = int((ref_1[sensor] + ref_2[sensor] + ref_3[sensor] + ref_4[sensor] + ref_5[sensor])/5)
        ref_avg.append(ref_sum)
    while True:
        current = read_pressure(outputs, inputs)
        is_on = [ False, False, False, False ]
        for index in range(len(current)):
            current[index] -= ref_avg[index]
            is_on[index] = (current[index] > thresholds[index])
        
        print(ref_avg)  
        print(current) 
        print(thresholds)
        print(is_on)
        print('-----')

        

