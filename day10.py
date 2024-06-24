def apakah_prima(bilangan):
    if bilangan <= 1:
        print("bukan bilangan prima")
    elif bilangan == 2:
        print("bilangan prima")
    else:
        for i in range(2, bilangan):
            if bilangan % i == 0:
                print("bukan bilangan prima")
                return
        print("bilangan prima")
apakah_prima(7)  # Output: bilangan prima
apakah_prima(10) # Output: bukan bilangan prima
