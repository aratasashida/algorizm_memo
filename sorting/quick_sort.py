def quick_sort(target):
    # リストの長さが1以下の場合、ソーティングが済んでいる
    if len(target) <= 1:
        return target

    # ピポットの取得。今回は配列の始め。
    pivot = target[0]
    sorting_target = target[1:]
    # ソーティング処理
    small_list = [i for i in sorting_target if i <= pivot]
    large_list = [i for i in sorting_target if i > pivot]

    # 再起呼び出し
    return quick_sort(small_list) + [pivot] + quick_sort(large_list)

if __name__ == '__main__':
    test_list = [5, 3, 9, 10, 2, 7, 8, 8, 6, 13]
    print(quick_sort(test_list))

