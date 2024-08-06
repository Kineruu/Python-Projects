import simpleeval

def Calc(Equations):
    try:
        Equations.replace("^", "**")
        return simpleeval.simple_eval(Equations)
    except Exception as e:
        return e

UsersInput = input()
result = Calc(UsersInput)
print(result)

