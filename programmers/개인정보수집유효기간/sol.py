def solution(today, terms, privacies):
    answer = []
    
    #가입일자, 경과일, 현재날짜 주면 파기여부 반환해주는 함수
    def delete(pri, month, present):
        new_pri = pri.split('.')
        del_year = int(new_pri[0])
        del_month = int(new_pri[1])
        del_day = int(new_pri[2])
        del_month = del_month + int(month)
        while del_month > 12:
            del_year = del_year + 1
            del_month = del_month - 12
        if del_month < 10:
            str_month = '0' + str(del_month)
        else:
            str_month = str(del_month)
        if del_day < 10:
            str_day = '0' + str(del_day)
        else:
            str_day = str(del_day)
        str_year = str(del_year)
        
        deldate = str_year + str_month + str_day
        deldate = int(deldate)
        new_present = present[:4] + present[5:7] + present[8:]
        nowdate = int(new_present)
        if nowdate >= deldate:
            return True
        else:
            return False
    
    new_terms = { }
    for i in terms:
        list = i.split()
        new_terms[list[0]] = list[1]
    num = 1
    for i in privacies:
        list2 = i.split()
        day = list2[0]
        month = int(new_terms[list2[1]])
        if delete(day, month, today):
            answer.append(num)
        num = num + 1
        
    return answer
# 프라이버시의 각 문자열을 포문으로 돌린다.

# 텀스 내용을 딕셔너리화 해서 프라이버시의 텀을 개월수로 변환해준다.

# 날짜를 계산한다. 일자는 나중에 비교하면 되고, 수집일자를 리스트로 분할한다. 이후 월이 12초과시 12빼고 1년 더하면 된다.