import collections

my_list  = ['Tick', 'Tock', 'Tock'] # 나의 리스트
new_list = ['Tick', 'Tock', 'Song'] # 추가로 나타난 리스트

counter1 = collections.Counter(my_list) # 리스트에 들어있는 원소의 개수 알아서 계산
counter2 = collections.Counter(new_list)

answer = collections.Counter(my_list) - collections.Counter(new_list) # 카운터 객체도 빼기가 가능함

print(counter1) # Counter({'Tock': 2, 'Tick': 1})
print(counter2) # Counter({'Tick': 1, 'Tock': 1, 'Song': 1})

print(counter1 - counter2) # Counter({'Tock': 1}) -> 'Tock' 2개에서 1개 빼서 결과가 1개만 남은걸로 나옴
print(counter2 - counter1) # Counter({'Song': 1})

print(answer) # Counter({'Tock': 1})
print(list(answer)[0]) # counter <-> list 가능