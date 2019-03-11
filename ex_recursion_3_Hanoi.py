# 하노이의 탑

# O(2^n)
def hanoi(from_A, pass_B, to_C, num):
    if num == 1:
        #print('num이 1일 때')
        print(f'{from_A} -> {to_C}')
        #print()
        return
    
    #print('처음', from_A, to_C, pass_B, num, num-1)
    hanoi(from_A, to_C, pass_B, num-1)
    print(from_A, '->', to_C)
    #print('마지막', pass_B, from_A, to_C, num, num-1)
    hanoi(pass_B, from_A, to_C, num-1)

hanoi('A','B','C',3)