# https://leetcode.com/problems/daily-temperatures/

def temperatureCheck(temperatures):
    currentDay = 0
    stack = []
    result = [0] * len(temperatures)
    for t in temperatures:
        while stack and stack[-1][1] < t:
            prevDay, temperatur = stack.pop()
            result[prevDay] = currentDay - prevDay
        
        stack.append((currentDay, t))
        currentDay += 1
    
    return result

print(temperatureCheck([73, 74, 75, 71, 69, 72, 76, 73]))