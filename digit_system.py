def to_scale_notation(n, to_base, from_base=10):
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if not 1 <= to_base <= 36:
        return False
    if not 1 <= from_base <= 36:
        return False
    try:
        if from_base == 1:
            n = len(n)
        else:
            n = int(str(n), from_base)
    except Exception as e:
        return False
    if to_base == 1:
        return '0' * n
    if n < to_base:
        return alphabet[n]
    else:
        return to_scale_notation(n // to_base, to_base) + alphabet[n % to_base]


to_scale_notation(n=int(input()), to_base=int(input()))
