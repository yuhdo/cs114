
#Ask the user for a distance, then the units of that distance, then the target units. Then print out the conversion as below.
print('tell me a numarical distince')
dis_num = int(input())
print('km, or mi,ft and m?')
start = input()
if start == 'km':
    
    mi_num = float(dis_num * 1.60934)

    print(mi_num)

else:
    km_num = float(dis_num / 1.60934)

    print(km,_num)

#Enter a distance: 100 Enter units: mi Enter target units: km 100 mi is 160.93440000000115 km


