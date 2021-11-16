def p_a():
    arr=[1,2,3,4,4,5,5]
    print(len(set(arr)))

def p_b():
    arr=[1,2,3]
    arr_1=[4,3,2]
    print(set(arr).intersection(arr_1))
def p_c():
    arr = [1, 3, 2]
    arr_1 = [4, 3, 2]
    a=list(set(arr).intersection(arr_1))
    print(a.sort())
def p_d():
    numbers=[1,2,3,4,3,2,1]
    occur_before = set()
    for num in numbers:
        if num in occur_before:
            print('YES')
        else:
            print('NO')
            occur_before.add(num)

def p_f():
    list=['white','black','yellow','yellow']
    print(len(set(list)))


if __name__ == '__main__':
    p_f()