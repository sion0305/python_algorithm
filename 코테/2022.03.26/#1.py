import re
def solution(logs):
    answer = 0
    log_message = ["team_name", "application_name", "error_level", "message"]
    
    for log in logs:
        if len(log) > 100: # 100자 넘김
            answer += 1
            continue
        format = True
        for m in log_message: # 빠진 수집
            if m not in log:
                answer += 1
                format = False
                break
        if format == False:
            print('폼', log)
            continue
        log_split = log.split(' : ')
        # print(log_split)
        
        for i, s in enumerate(log_split):
            s_split = s.split(' ')
            if i == 0:
                if len(s_split) >=2:
                    answer += 1
                    break
            else:
                if len(s_split) > 2: # 메세지에 공백이 있을 경우
                    print('공백', log)
                    answer += 1
                    break
                if not s_split[0].isalnum(): # 특수문자 있는 경우
                    print('특', log)
                    answer += 1
                    break
                if bool(re.search('\d', s_split[0])): # 숫자 있는 경우
                    print('dig',log)
                    answer += 1
                    break

    return answer


# logs = ["team_name : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange", "no such file or directory", "team_name : recommend application_name : recommend error_level : info message : RecommendSucces11", "team_name : recommend application_name : recommend error_level : info message : Success!", " team_name : db application_name : dbtest error_level : info message : test", "team_name    : db application_name : dbtest error_level : info message : test", "team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"]
logs = ["team_name : db application_name : dbtest error_level : info message : test", "team_name : test application_name : I DONT CARE error_level : error message : x", "team_name : ThisIsJustForTest application_name : TestAndTestAndTestAndTest error_level : test message : IAlwaysTestingAndIWillTestForever", "team_name : oberervability application_name : LogViewer error_level : error"]
print(solution(logs))