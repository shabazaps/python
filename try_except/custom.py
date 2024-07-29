# def custom(x):
#     if x<0:
#         raise Exception("Number should be non-negative")
# try:
#     num = int(input("Enter a number: "))
#     custom(num)
# except Exception as e:
#     print(f"Custom Exceoption caught: {e}")
#
#
def custom(x):
    if x < 0:
        raise Exception("Number should be Positive!!")
    try:
        num = int(input("Enter a Number: "))
        custom(num)
    except Exception as e:
        print(f"Exception caught: {e}")

custom(43)
