def withdraw(balance,request):
    print("Current balance = " + str(balance))
    if request > balance:
        print("Can`t give you all this money !!")
        print(" ")
    elif request <= 0:
        print("More than zero plz!")
        print(" ")
    else:
        while request > 0:
            if request >= 100:
                request -= 100
                print("give 100")
            elif request >= 50:
                request -= 50
                print ("give 50")
            elif request >= 10:
                request -= 10
                print ("give 10")
            elif request >= 5:
                request -= 5
                print ("give 5")
            else:
                print ("give " + str(request))
                request = 0
        print(" ")
        return request
    

balance = 500
withdraw(balance,277)
withdraw(balance,30)
withdraw(balance,5)
withdraw(balance,700)
withdraw(balance,-10)

