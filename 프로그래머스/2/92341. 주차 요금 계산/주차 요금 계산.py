# from math import ceil

# def solution(fees, records):
#     answer = []
#     cars = {}  # {차량 번호: [출입시간]}
#     times = {}  # {차량 번호: 주차시간 총합}
#     basic_time, basic_fee, unit_time, unit_fee = fees

#     for r in records:
#         time, car_num, go_type = r.split()
#         if not car_num in cars:
#             cars[car_num] = []
#         cars[car_num].append(time)

#     for num, time_record in cars.items():
#         if len(time_record) % 2 == 1:
#             time_record.append('23:59')
#         total_time = 0
#         for i in range(0, len(time_record), 2):
#             in_time, out_time = time_record[i], time_record[i+1]
#             in_h, in_m = map(int, in_time.split(':'))
#             out_h, out_m = map(int, out_time.split(':'))
#             total_time += (60 * (out_h - 1 - in_h) + (out_m + 60 - in_m))
#         times[num] = total_time

#     for a in sorted(times.keys()):
#         total_time = times[a]
#         if total_time <= basic_time:
#             answer.append(basic_fee)
#         else:
#             answer.append(basic_fee + ceil((total_time - basic_time) / unit_time) * unit_fee)

#     return answer

from collections import defaultdict
import math

def solution(fees, records):
    # 기본 시간, 기본 요금, 단위 시간, 단위 요금
    basic_time, basic_fee, unit_time, unit_fee = fees
    cars = {}  # 차마다 정보 저장
    result = []  # 요금 리스트
    last_time = 23 * 60 + 59  # 23:59
    
    # 차 번호마다의 기록 저장
    for r in records:
        time, car_num, enter_type = r.split()  # 시각, 차 번호, 출입 종류
        minute = 0  # 시각을 분으로 변경
        minute += (int(time[:2]) * 60 + int(time[3:]))
        
        # cars에 없는 차라면 추가
        if car_num not in cars:
            cars[car_num] = []
            
        cars[car_num].append((minute, enter_type))
        
    cars = sorted(cars.items())  # 키 오름차순으로 정렬
    
    for car_num, history in cars:
        parking_time = 0  # 주차되어 있던 시각
        
        # 들어간 시각 기준
        for idx in range(0, len(history), 2):
            # 만약 마지막 출차가 없다면 -> 23:59로 처리
            if idx == len(history) - 1 and len(history) % 2 != 0:
                parking_time += (last_time - history[idx][0])
            else:
                parking_time += (history[idx+1][0] - history[idx][0])
                
        fee_time = parking_time - basic_time  # 기본 시간 제외하고 요금 내야하는 시간
        fee = basic_fee  # 기본 요금으로 초기화
        
        # 기본 시간보다 적게 주차했다면 0으로 
        fee_time = max(fee_time, 0)
        
        # if fee_time % unit_time == 0:  # 단위 시간으로 나누어 떨어지면
        #     fee += (fee_time // unit_time) * unit_fee
        # else:  # 단위 시간으로 나누어 떨어지지 않으면
        #     fee += (fee_time // unit_time + 1) * unit_fee
        
        # 단위 시간으로 나눠떨어지지 않으면 올림
        fee += math.ceil(fee_time / unit_time) * unit_fee
        
        result.append(fee)
    
    return result
        
    