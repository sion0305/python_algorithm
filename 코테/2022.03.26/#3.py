def solution(num_teams, remote_tasks, office_tasks, employees):
    answer = []
    team_remote = [[] for row in range(num_teams+1)]
    team_office = [[] for row in range(num_teams+1)]

    for i, em in enumerate(employees):
        temp = em.split()
        team_num = int(temp[0])
        remotable = True
        for j in range(1, len(temp)):
            if temp[j] in office_tasks:
                remotable = False
        if remotable == True:
            team_remote[team_num].append(i+1)
        else:
            team_office[team_num].append(i+1)

    for i in range(1, num_teams+1):
        print(team_office[i])
        print(team_remote[i])
        if len(team_office[i]) == 0 and len(team_remote[i]) > 0:
            team_remote[i].remove(min(team_remote[i]))
        answer.extend(team_remote[i])
    return answer

num = 2
remote = ["design"]
office = ["building", "supervise"]
employees = ["2 design", "1 supervise building design", "1 design", "2 design"]

print(solution(num, remote, office, employees))