def differencing(series, order):
    result = list(series)  # đảm bảo là list
    for _ in range(order):
        if len(result) <= 1:
            return []  # nếu không đủ để diff nữa
        new_result = []
        for i in range(1, len(result)):
            new_result.append(result[i] - result[i-1])
        result = new_result
    return result