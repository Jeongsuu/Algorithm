def solution(n, lost, reserve):
    #겹치는 원소 제거
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    #비교하며 체육복 빌리기
    for res_val in set_reserve:
        if res_val-1 in set_lost:
            set_lost.remove(res_val-1)
        elif res_val+1 in set_lost:
            set_lost.remove(res_val+1)
    return n - len(set_lost)