

def Heart_Plot():
    y = 2.5
    #x = -3
    while y >= -1.6:
        y = y - 0.2
        x = -3.6
        one_floor = ""
        while x <= 4.8:
            #x = x + 0.1
            if (x*x + y*y -1)**3 <= 3.6*x*x*y*y*y \
                or (y >-1 and y <-0.8 and x <3.7 and x >2.2) \
                or (x > -2.5 and x <-2.1 and y <1.5 and y >-1) \
                or (((x<2.5 and x>2.2) or (x>3.4 and x<3.7)) and y>-1 and y<1.5):
                one_floor = one_floor + " "
            else:
                one_floor = one_floor + "*"
            x = x + 0.1
            #    print(" ")
            #else:
            #    print("*")
        print(one_floor)
    #print("\n")


Heart_Plot()
