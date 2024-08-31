def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        j = i + 1
        while j < len(numbers):
            num = numbers[i] + numbers[j]
            if num not in answer:
                answer.append(num)
            j = j + 1
    answer.sort()
    return answer