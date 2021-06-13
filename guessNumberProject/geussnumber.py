import random



con = True

while con:
    x = random.randint(0,1000)
    print(x)
    print("guess number")
    print("you have 3 tries .")
    n = int(input('>'))
    tries = 3


    if x==n:
        print("good job you guessed the number ")
        ch = input("do you wanna continue playing ? type Y or N\n")
        if ch == 'N':
            break
        else:
            pass

    else:

            tries -=1
            print(f"you have {tries} left")
            print(f"this number is between {x-random.randint(1,10)} and {x+random.randint(1,10)} ")
            print("guess it ")
            n = int(input(">"))
            if n == x :
                print("good job ")
                ch = input("do you wanna continue playing ? type Y or N\n")
                if ch == 'N':
                    con = False
                    break

                else:
                    print("nw")
            else:
               if x%2 == 0:
                   print("this number is pair")
                   print("guess it ")
                   n = int(input(">"))
                   if n == x :
                       print("good job ")
                       ch = input("do you wanna continue playing ? type Y or N\n")
                       if ch == 'N':
                           con = False
                           break

                       else:
                           print("now new number to guess")
                   else:
                         l = ['/','+','-','*']
                         print(f"if we did on of those operations + / * - with the unkown number and other number which is betwenn 10 and 1 it gives  ")
                         print("the result is :")
                         g = random.randint(0,3)
                         f = random.randint(1,10)

                         if l[g] == '/':
                             print(x/f)
                         elif l[g] == '+':
                             print(x+f)
                         elif l[g] == '-':
                             print(x-f)
                         else:S
                             print(x*f)
                         print("guess it ")
                         print(f"g == {g} f == {f} ")
                         n = int(input(">"))
                         if n == x :
                             print("good job ")
                             ch = input("do you wanna continue playing ? type Y or N\n")
                             if ch == 'N':
                                 con = False
                                 break

                             else:
                                 print("now new number")

                         else:
                             print(f"unfortunately u lose the correct number is {x}")
                             ch = input("do you wanna continue playing ? type Y or N\n")
                             if ch == 'N':
                                 con = False
                                 break

                             else:
                                 print("now new number")


               else:
                   print("this number is umpair")
                   print("guess it ")
                   n = int(input(">"))
                   if n == x :
                       print("good job ")
                       ch = input("do you wanna continue playing ? type Y or N\n")
                       if ch == 'N':
                           con = False
                           break

                       else:
                           print("now new number")

                   else:
                        l = ['/','+','-','*']
                        print(f"if we did on of those operations + / * - with the unkown number and other number which is between 10 and 1 it gives the result below: ")
                        print("the result is :")
                        g = random.randint(0,3)
                        f = random.randint(1,10)

                        if l[g] == '/':
                            print(x/f)
                        elif l[g] == '+':
                            print(x+f)
                        elif l[g] == '-':
                            print(x-f)
                        else:
                            print(x*f)
                        print("guess it ")
                        print(f"g == {g} f == {f} ")
                        n = int(input(">"))
                        if n == x :
                            print("good job ")
                            ch = input("do you wanna continue playing ? type Y or N\n")
                            if ch == 'N':
                                con = False
                                break

                            else:
                                print("now new number")

                        else:
                            print(f"unfortunately u lose the correct number is {x}")
                            ch = input("do you wanna continue playing ? type Y or N\n")
                            if ch == 'N':
                                con = False
                                break

                            else:
                                print("now new number")
