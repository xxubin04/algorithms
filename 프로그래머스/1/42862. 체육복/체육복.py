def solution(n, lost, reserve):
    student = [1] * n
    
    for l in lost:
        student[l-1] -= 1
    
    for r in reserve:
        student[r-1] += 1
    
    for s in range(n):
        if student[s] == 2:  # 여분의 체육복이 있다면
            if s == 0 and student[1] == 0:  # 첫 번째 학생이고 다음 학생이 없다면
                student[0] = 1
                student[1] = 1
            elif s == n-1 and student[n-2] == 0:  # 마지막 학생이고 이전 학생이 없다면
                student[n-1] = 1
                student[n-2] = 1
            elif 0 < s < n-1:
                if student[s-1] == 0:  # 왼쪽 학생이 없다면 줌
                    student[s] = 1
                    student[s-1] = 1
                elif student[s+1] == 0:  # 오른쪽 학생이 없다면 줌
                    student[s] = 1
                    student[s+1] = 1
            
            # 체육복을 줄 학생이 없는 여분의 체육복이 있는 학생은 1 처리(계산 쉽게 하려고)
            if student[s] == 2:
                student[s] = 1
    
    return sum(student)
                
                
            
            
                