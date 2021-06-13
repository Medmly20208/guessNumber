def Checkint(s):
    """
     this function is set to check if the input is an integer if it is an
     integer the loop will break if not the proccess is repeated
     it takes on parameter which is the string that's gonna show
     before inputting the variable
     """
    condition = True
    while condition:
        try:
            print(s)
            k = int(input('>'))
        except ValueError:
            print("unvalid input please enter integer value")

        else:
            condition = False


    return k
