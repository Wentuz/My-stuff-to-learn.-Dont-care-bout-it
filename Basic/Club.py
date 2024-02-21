def is_bob(name: str) -> bool:
    if name.lower() == 'bob':
        return True
    else:
        return False
    
def is_an_adult(age: int, has_id: bool) -> bool:
    if age >= 18 and has_id == True:
        return True
    else:
        return False


def main(name: str, age: int, has_id: bool) -> None:
    if is_bob(name) == True:
        print("Get out of here Bob!")
        return
    if is_an_adult(age, has_id) == True:
        print("You may enter the club!")
        return
    else:
        print("You may not enter the club!")
        return


if __name__ == '__main__':
    main('Bob', 27, True)
    main('Kate', 27, True)
    main('Adam', 16, False)
    main('Mike', 21, False)