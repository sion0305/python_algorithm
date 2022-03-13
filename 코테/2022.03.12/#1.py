def solution(money, costs):
    change = [500, 100, 50 ,10, 5, 1]
    count = []
    costs.reverse()

    for i in range(len(change)-1):
        now = money // change[i] * costs[i]
        next = money // change[i+1] * costs[i+1]
        
        if money % change[i] == 0 or money % change[i+1] == 0:
            count.append(min(now + money % change[i] * costs[i+1], next))
        else:
            if now > next:
                count.append(0)
                continue
            else:
                count.append(now)
                money %= change[i]

    print(count)

    return sum(count)

money = int(input())
costs = list(map(int, input().split()))

print(solution(money, costs))