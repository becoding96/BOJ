def solution(id_list, report, k):
    report_dic = {id:[0, set()] for id in id_list}  # id인 유저: [신고받은 횟수, {id를 신고한 유저들 명단}]
    answer = [0 for _ in range(len(id_list))]
    
    for r in report:
        f, t = r.split()
        if f not in report_dic[t][1]:  # 중복 신고 방지, 신고한 유저들 명단에 없으면
            report_dic[t][0] += 1  # 신고받은 횟수 증가
            report_dic[t][1].add(f)  # 신고한 유저 명단에 추가
    
    # print(report_dic)
            
    for v in report_dic.values():  # v = [신고받은 횟수, {id를 신고한 유저들 명단}]
        if v[0] >= k:  # 신고받은 횟수가 k보다 같거나 크면
            for name in v[1]:  # 신고한 유저들 명단 순회하면서
                answer[id_list.index(name)] += 1  # 메일 수 증가시켜줌
            
    return answer