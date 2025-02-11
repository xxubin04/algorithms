# 이것이 코테다 p.180
# Ch.6 정렬
# 실전 문제 3. 성적이 낮은 순서로 학생 출력하기
# 걸린 시간: 6분 29초
# 일시: 2025.02.11

info = {}  # (학생 이름 : 학생 성적)

for _ in range(n := int(input())):
    name, score = input().rstrip().split()  # 이름, 성적 입력받음
    info[name] = int(score)

# 성적을 기준으로 내림차순 정렬
# sorted 함수는 딕셔너리의 키들을 정렬된 리스트로 반환
result = sorted(info, key=lambda x: info[x], reverse=True)

for i in result:
    print(i, end=' ')
