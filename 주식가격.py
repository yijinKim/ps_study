from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        cnt = 0
        temp = prices.popleft()
        for price in prices:
            cnt += 1
            if temp > price:
                break
        answer.append(cnt)
    
    return answer

def solution2(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            answer[i] += 1
            if prices[i] > prices[j]:
                break
    return answer

print(solution2([1,2,3,2,3]))