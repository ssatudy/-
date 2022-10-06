import sys; sys.stdin = open('input_벌꿀채취.txt', 'r')
from itertools import combinations

def comb(nums):
    candi_cnt = 0
    for k in range(1, M+1):
        aa = list(combinations(nums, k))

        for num in aa:
            tmp_cnt = 0
            if sum(num) > C:
                continue
            for l in range(k):
                tmp_cnt += num[l-1]**2
            candi_cnt = max(candi_cnt, tmp_cnt)
    return candi_cnt


for tc in range(int(input())):
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]

    rst_nums = []
    rst_idx = []
    rst_cnt = 0
    for i in range(N):
        for j in range(N-M+1):
            tmp_idx = []
            tmp_nums = []
            tmp_cnt = 0
            for m in range(M):
                tmp_idx.append((i, j+m))
                tmp_nums.append(honey[i][j+m])
            if sum(tmp_nums) <= C:
                for num in tmp_nums:
                    tmp_cnt += num**2
            elif sum(tmp_nums) > C:
                tmp_cnt = comb(tmp_nums)
            if rst_cnt < tmp_cnt:
                rst_cnt = tmp_cnt
                rst_nums = tmp_nums
                rst_idx = tmp_idx
    # print(rst_cnt)
    # print(rst_nums)
    # print(rst_idx)
    while rst_idx:
        r, c = rst_idx.pop()
        honey[r][c] = -1
    # for line in honey:
    #     print(line)
    rst2_nums = []
    rst2_idx = []
    rst2_cnt = 0
    for i in range(N):
        for j in range(N - M + 1):
            tmp_idx = []
            tmp_nums = []
            tmp_cnt = 0
            for m in range(M):
                tmp_idx.append((i, j + m))
                tmp_nums.append(honey[i][j + m])
            if -1 in tmp_nums:
                continue
            if sum(tmp_nums) <= C:
                for num in tmp_nums:
                    tmp_cnt += num ** 2
            elif sum(tmp_nums) > C:
                tmp_cnt = comb(tmp_nums)
            if rst2_cnt < tmp_cnt:
                rst2_cnt = tmp_cnt
                rst2_nums = tmp_nums
                rst2_idx = tmp_idx
    # print(rst2_nums)
    # print(rst2_cnt)
    print(f'#{tc+1}', rst_cnt+rst2_cnt)



