def find_keywords(good):
  length = len(good)
  return [good[i:j + 1] for i in range(length) for j in range(i,length)]

def filter_list(unique):
    if not unique:
        return ["None"]
    result = []
    min_len = min(unique,key =len)
    for u in unique:
        if len(u) == len(min_len):
            result.append(u)
    return set(result)

def solution(goods):
    answer = []
    copy_goods = list(goods)
    for g in goods:
        unique = []
        copy_goods = list(goods)
        keywords = find_keywords(g)
        copy_goods.remove(g)
        temp = ' '.join(s for s in copy_goods)
        for key in keywords:
            if key not in temp:
                unique.append(key)
        unique = filter_list(unique)
        answer.append(' '.join(s for s in sorted(unique)))
    return answer




# goods = ["abcdeabcd", "cdabe", "abce", "bcdeab"]
goods = ["pencil", "cilicon", "contrabase", "picturelist"]
# print(find_keywords(goods[0]))
print(solution(goods))
