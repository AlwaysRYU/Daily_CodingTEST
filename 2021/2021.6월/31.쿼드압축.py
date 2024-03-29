# 쿼드 압축
# https://programmers.co.kr/learn/courses/30/lessons/68936

def solution(arr):
    answer = [0,0]
    NN = len(arr[0])//2
    print(NN)

    def gumsa(x,y,n):
        bunri = False
        Yes = arr[x][y]
        print(str(x) + str(y) + " 왼쪽위의 수 " + str(Yes))
        if n == 1: # n이 1일 경우에는 answer에다가 값을 넣는다.
            print("N은 1이다.")
            print(str(x) + " " + str(y) + "는 분리되지 않는다.")
            if Yes == 0 :
                answer[0] += 1
            else:
                answer[1] += 1
        else :
            for i in range(n):
                for j in range(n):
                    if arr[x+i][y+j] != Yes :
                        print("다르다!")
                        gumsa(x, y, n//2)
                        gumsa(x + n//2, y, n//2)
                        gumsa(x, y + n//2, n//2)
                        gumsa(x + n//2, y + n//2, n//2)
                        bunri = True
            if bunri == False :  
                print("병합한다!")  
                if Yes == 0 :
                    answer[0] += 1
                else:
                    answer[1] += 1

    gumsa(0,0,NN)
    print()
    print("--")
    print()
    gumsa(NN,0,NN)
    print()
    print("--")
    print()
    gumsa(0, NN, NN)
    print()
    print("--")
    print()
    gumsa(NN,NN,NN) 
    print(str(NN) + " 을 확인하세요")
    return answer

A1 = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
A2 = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]

print(solution(A1))
# print(solution(A2))