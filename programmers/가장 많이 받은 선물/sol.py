def solution(friends, gifts):
    answer = 0
    def present_score(name, my_gifts):
        num = 0
        for i in my_gifts:
            if (name + " ") in i:
                num = num + 1
            elif (" " + name) in i:
                num = num - 1
        return num
    presentscore = {}
    
    for i in friends:
        presentscore[i] = present_score(i, gifts)
    #선물지수 만들었고, 개인지수 만들기
    #무지가 라이언에게 선물을 받을지말지 = muzi ryan > ryan muzi / muzi ryan = ryan muzi and presentscore[muzi]>presentscore[ryan]을 만족하면 선물을 하나 받는거지, 받으면 딕트의 키 값을 한개 플러스한다. 마지막에는 마이맥스로 찾고. 반복을 어떻게 때릴 것인가? 리스트의 한명에게 리스트 전부를 반복하면 된다. 그럼 포 공장을 하나 더 만들어야겠네. 이 공장은 무슨 공장인가, 무지가 선물을 몇개 받을지 결정해주는 공장이다. 리턴값은 무지가 받는 선물 개수이다. 이걸 위해서는 프렌즈목록 기프트목록 바딕
    
    result = {}
    max_num = len(friends)
    for x in friends:
        num = 0
        myscore = 0
        while num != max_num:
#무지는 frineds[0], 라이언은 friends[1], 프로도는 2 네오는 3
#즉 무지라이언은 프렌즈0프렌즈1
            if x == friends[num]:
                pass
            elif gifts.count(x + " " + friends[num]) > gifts.count(friends[num] + " " + x):
                myscore = myscore + 1
            elif gifts.count(x + " " + friends[num]) == gifts.count(friends[num] + " " + x):
                if presentscore[x] > presentscore[friends[num]]:
                    myscore = myscore + 1
            num = num + 1
            
            result[x] = myscore

    list_score = []
    for cat in result:
        list_score.append(result[cat])
    answer = max(list_score)
        
    return answer