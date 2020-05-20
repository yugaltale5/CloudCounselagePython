def sum_series(n):
    if n !=0:
        return n+sum_series(n-2)
    else:
        return 0
if __name__=="__main__":
    print(sum_series(6))
    print(sum_series(10))
