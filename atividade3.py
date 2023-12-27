def dividers_of_a_number(n: int) -> list[int]:
    dividers = []
    for i in range(1,n+1):
        if n % i == 0:
            dividers.append(i)
    return dividers