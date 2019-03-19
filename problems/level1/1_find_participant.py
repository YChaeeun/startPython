
import collections

def solution_1(participant, completion):

    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


def solution_2(participant, completion) :
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i] :
            return participant[i]
    return participant[len(participant)-1]

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "mislav", "ana"]

print(solution_1(participant, completion))

print(solution_2(participant, completion))





