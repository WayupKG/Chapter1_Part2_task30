def count_func():
    list_ = [5, 5, 7, 9, 8, 7, 8, 7]
    res_list = list(set(list_))
    for l in res_list:
        res = list_.count(l)
        print(f'Вы спиcке {res} повторяющихся  {l}')
count_func()