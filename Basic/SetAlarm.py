def set_alarm(employed, vacation):
    if employed == True and vacation == False:
        return True
    else:
        return False

if __name__ == "__main__":
    print(set_alarm(True, True))
    print(set_alarm(True, False))
    print(set_alarm(False, True))
    print(set_alarm(False, False))