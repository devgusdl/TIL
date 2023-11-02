# https://www.acmicpc.net/problem/1546
 
#시험 본 과목의 개수 입력
N = int(input())

# 세준이의 현재 성적을 리스트로 입력받음
scores = list(map(int, input().split()))

# 최대값(M) 계산
M = max(scores)

# 새로운 점수로 변환하고 리스트에 저장
new_scores = [(score / M) * 100 for score in scores]

# 평균 계산
new_average = sum(new_scores) / N

# 결과 출력
print("{:.2f}".format(new_average))


N = int(input())
scores = list(map(int, input().split()))

for score in scores:
    print(score)