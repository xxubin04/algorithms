input = open(0).readline 

sensor_num = int(input()); center_num = int(input())
sensor_location = sorted(list(map(int, input().split())))
sensor_gap = sorted([sensor_location[i] - sensor_location[i-1] for i in range(1, sensor_num)], reverse=True)
print(sensor_location[-1] - sensor_location[0] - sum(sensor_gap[:center_num-1]))