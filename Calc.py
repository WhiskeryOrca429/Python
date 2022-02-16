import time

def Calc():
    print("[Calculator]")
    num1 = input("[First Number?]:")
    oper = input("[Operator?]:")
    num2 = input("[Second Number?]:")

    num1 = float(num1)
    num2 = float(num2)

    
    if oper == ("+"):
        asn1 = num1 + num2
        print("[Answer]:",asn1)
    
    if oper == ("-"):
        asn2 = num1 - num2
        print("[Answer]:",asn2)

    if oper == ("/"):
        asn3 = num1 / num2
        print("[Answer]:",asn3)

    if oper == ("*"):
        asn4 = num1 + num2
        print("[Answer]:",asn4)

    time.sleep(3)
    Calc()

Calc()
