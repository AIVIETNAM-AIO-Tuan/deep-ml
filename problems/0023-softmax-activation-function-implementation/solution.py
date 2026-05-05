import math

def softmax(scores: list[float]) -> list[float]:
    total = sum(math.exp(i - max(scores))for i in scores)
    result = []
    for i in scores:
        i = math.exp(i-max(scores))/total
        result.append(i)
    return result