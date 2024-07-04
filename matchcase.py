inputvar=int(input("Enter a number between 1 and 3:"))
#match case
match inputvar:
    #pattern1
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case _:
        print("number not between 1 and 3")
              
        
