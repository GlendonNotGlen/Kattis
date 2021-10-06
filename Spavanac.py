
def main():
    given = input()
    time = given.split(" ")
    hours = int(time[0])
    minutes = int(time[1])
    newMinutes = minutes - 45
    if newMinutes < 0:
        hours -= 1
        newMinutes = 60 + newMinutes
        if hours < 0:
            hours = 23

    print(str(hours) + " " + str(newMinutes))



if __name__ == '__main__':
    main()