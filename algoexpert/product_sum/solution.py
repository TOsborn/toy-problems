

def productSum(array):
    def rec(array, depth):
        if type(array) is int:
            return array
        if array == []:
            return 0
        
        return (depth+1)*sum(rec(val, depth+1) for val in array)

    return rec(array, 0)


if __name__ == '__main__':
    print(productSum([1]))
