def binary_search(array, target) :

    start = 0

    end = n - 1

    while start <= end :

        mid = (start + end) // 2

        if array[mid] == target :

            return True

        elif array[mid] > target :

            end = mid - 1

        else :

            start = mid + 1

    return None


n = int(input())

n_arr = sorted(list(map(int, input().split())))

m = int(input())

m_arr = list(map(int, input().split()))


for i in range(m) :

    if binary_search(n_arr, m_arr[i]) :

        print(1)

    else :

        print(0)