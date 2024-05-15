def check_exam(arr1, arr2):
    score = 0
    x = 0
    for y in arr1:
        if arr2[x] == " ":
            score = score
        elif arr2[x] == arr1[x]:
            score = score + 4
        else:
            score = score - 1
        x = x + 1
    return score

if __name__ == "__main__":
    print(check_exam(["a", "a", "b","b"], ["a", "c", "b", "d"]))