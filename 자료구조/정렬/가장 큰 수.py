def solution(numbers):
    numbers = list(map(str, numbers)) #	['6', '10', '2']	
    numbers.sort(key=lambda x : x * 3, reverse = True) # ['6', '2', '10']
    return str(int(''.join(numbers)))