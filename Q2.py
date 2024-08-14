def shots(T, test_cases):
    res = []
    for case in test_cases:
        N, K, heights = case #N=number of players between ali and gi-hun, K = height of ali and gi-hun
        shots = sum(1 for h in heights if h > K)
        res.append(shots)
    return res
#T= number of test cases i,e (3)
T = int(input())
test_cases = []
for _ in range(T):
    N, K = map(int, input().split())
    heights = list(map(int, input().split()))
    test_cases.append((N, K, heights))

shot = shots(T, test_cases)

for res in shot:
    print(res)
