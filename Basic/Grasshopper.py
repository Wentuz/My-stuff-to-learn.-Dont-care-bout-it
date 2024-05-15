def get_grade(s1, s2, s3):
    avg = (s1 + s2 + s3) / 3
    if avg < 60:
        return 'F'
    elif avg < 70:
        return 'D'
    elif avg < 80:
        return 'C'
    elif avg < 90:
        return 'B'
    else:
        return 'A'

if __name__ == '__main__':
    print(get_grade(95, 90, 93))
    print(get_grade(70, 70, 70))