def solution(n, lost, reserve):
     
    _reserve = [x for x in reserve if x not in lost]  # 이거를 추가하는 게 뭐가 다르지??
    _lost = [x for x in lost if x not in reserve]
    
    num = n - len(_lost)
    
    for lostone in _lost :
        if lostone in _reserve :
            num += 1
            _reserve.remove(lostone)
        elif lostone-1 in _reserve :
            num += 1
            _reserve.remove(lostone-1)
        elif lostone+1 in _reserve :
            num += 1
            _reserve.remove(lostone+1)
    return num



def solution_2(n, lost, reserve):

    _reserve = [x for x in reserve if x not in lost]
    _lost = [x for x in lost if x not in reserve]

    for r in _reserve:
        front = r - 1
        back = r + 1

        if front in _lost:
            _lost.remove(front)
        elif back in _lost:
            _lost.remove(back)

    return n - len(_lost)