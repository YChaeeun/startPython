
##############################################

# filter(), map() => 데이터 전처리, 정제 등 처리시 사용
# filter() => 데이터를 거르는데 사용

# tmp = filter('조건을 처리하는 함수', '데이터 덩어리')

data = [1,2,34,5,4,-2, -1, 0, 2, 3]

def filterCB(d):  # 조건을 만족하면 True, 아니면 False를 리턴하게 구성
    return d<0

tmp = filter(filterCB, data)
print(data)
print(list(tmp))  #-2, -1

#filter()를 사용하면 원본대비 데이터의 모양이 변형된다
tmp = filter(filterCB, data)
print(len(data), len(list(tmp)))  # 10, 2

##############################################

# map() => 데이터 전체를 가공할때 
# 가공 후 데이터는 원본대비 동일한 shape를 가진다

def trans(num):
    if num < 0 :
        return 0
    return num

data2 = list(map(trans, data))
print(data2)    # [1, 2, 34, 5, 4, 0, 0, 0, 2, 3]

##############################################

# lambda()
# 메모리를 효율적으로 사용할 수 있게 해줌 (처리속도도 빨라)
# 단, 구현 내용에 따라 표현이 어렵거나 불가할 수 있음

print(list(map(lambda x: x/2, data2))) 
# [0.5, 1.0, 17.0, 2.5, 2.0, 0.0, 0.0, 0.0, 1.0, 1.5]

def nor(x):
    return x/2

print(list(map(nor,data2)))
# [0.5, 1.0, 17.0, 2.5, 2.0, 0.0, 0.0, 0.0, 1.0, 1.5]

##############################################