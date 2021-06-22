def twoSum(arr, target):
    lookUp = {}
    for index, number in enumerate(arr):
        if number not in lookUp:
            lookUp[target - number] = index
        elif number in lookUp:
            return (number, arr[lookUp[number]])
    return ()
