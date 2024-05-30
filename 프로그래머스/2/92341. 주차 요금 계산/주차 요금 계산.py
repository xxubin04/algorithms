# from math import ceil

# def solution(fees, records):
#     cnt = 0
#     answer = []
#     cars = {}
#     cars_record = [[] * 1000]  # IN 기록만 저장 
#     times = []
#     basic_time, basic_fee, unit_time, unit_fee = fees
#     for r in records:
#         time, car_num, go_type = r.split()
        
#         if not int(car_num) in cars:  # 처음 방문하는 차량일 때
#             cars[int(car_num)] = cnt  # (차 번호 : 인덱스)로 저장  
#         else:  # 이미 방문한 적 있는 차량일 때 
#             cars_record[cars[int(car_num)]].append(time)  # 시간만 저장 
#     cars_record.sort()
#     cars = sorted(cars.items(), key=lambda item: item[0], reverse=True)
#     for i in range(len(cars_record)):
#         if len(cars_record[i]) % 2 == 1:  # 시간이 홀수개라면
#             cars_record[i].append('23:59')
#     for j in range(len(cars_record)):
#         time_amount = 0
#         for k in range(0, len(cars_record[j])-1, 2):
#             prior_time, later_time = cars_record[k], cars_record[k+1]
#             p_h, p_m = map(int, prior_time.split(':'))
#             l_h, l_m = map(int, later_time.split(':'))
#             time_amount += (60 * (l_h - 1 - p_h) + (l_m + 60 - p_m))
#         time.append(time_amount)
#     for p in range(len(time)):
#         if time[p] <= basic_time:
#             answer.append(basic_fee)
#         else:
#             answer.append(basic_fee + ceil(time[p]-basic_time)/unit_time * unit_fee)
#     return answer

from math import ceil

def solution(fees, records):
    answer = []
    cars = {}  # 차량 번호와 입출 시간 기록
    times = {}  # 차량 번호와 주차 시간 합계
    basic_time, basic_fee, unit_time, unit_fee = fees

    for r in records:
        time, car_num, go_type = r.split()
        if car_num not in cars:
            cars[car_num] = []
        cars[car_num].append(time)

    for car_num, time_records in cars.items():
        if len(time_records) % 2 == 1:
            time_records.append('23:59')
        total_time = 0
        for i in range(0, len(time_records), 2):
            in_time = time_records[i]
            out_time = time_records[i + 1]
            in_h, in_m = map(int, in_time.split(':'))
            out_h, out_m = map(int, out_time.split(':'))
            total_time += (out_h * 60 + out_m) - (in_h * 60 + in_m)
        times[car_num] = total_time

    for car_num in sorted(times.keys()):
        total_time = times[car_num]
        if total_time <= basic_time:
            total_fee = basic_fee
        else:
            total_fee = basic_fee + ceil((total_time - basic_time) / unit_time) * unit_fee
        answer.append(total_fee)

    return answer
