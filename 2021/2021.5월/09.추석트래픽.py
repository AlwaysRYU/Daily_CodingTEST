# 추석트래픽
# https://programmers.co.kr/learn/courses/30/lessons/17676?language=python3
# level3

t1 = ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]
t2 =  ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
t3 = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]

# 1초는 1000 밀리초

from collections import deque
from datetime import datetime

def solution(lines):
    answer = 0

    queue = deque()

    
    #시간 정리
    for i in range(len(lines))
        a =lines[i].split(" ")
        kizun = datetime.strptime(a[1],"%H:%M:%S.%f")
        plus = datetime.strptime(a[2][:-1], "%S.%f")
        print(kizun)
        print(plus)

    return answer


print(solution(t1))
#print(solution(t2))