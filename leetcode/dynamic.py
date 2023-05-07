# https://leetcode.com/problems/climbing-stairs/


memo = {1:1, 2:2}

def topDown(n):
    if n not in memo:
        memo[n] = topDown[n-1] + topDown[n-2]

    return memo[n]


def downTop(n):
    
    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2]

    return memo[n]