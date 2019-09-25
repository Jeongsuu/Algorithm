import collections
def solution(participant, completion):
    ans = collections.Counter(participant) - collections.Counter(completion)
    return list(ans.keys())[0]