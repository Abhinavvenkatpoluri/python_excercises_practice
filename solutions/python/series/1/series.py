def slices(series, length):
    # 1. Validation checks up front
    if not series:
        raise ValueError("series cannot be empty")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")

    # 2. Extract the slices
    result = []
    # We stop the loop early enough so the last slice fits perfectly
    for i in range(len(series) - length + 1):
        result.append(series[i : i + length])
        
    return result
