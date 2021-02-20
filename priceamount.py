# import * from Swiggy


# def priceamount():  # This method will shows the amount to be paidprint("\n")

#     amount = 0
#     ordered = []
#     count = 0

#     print("YOU ORDERED LIMIT IS 3")
#     print()

#     while True:
#         if count == 3:
#             break
#         else:
#             select = input("If you want to place your oder please press Y or N for not. :")
#             if select == "Y" or "y":
#                 dish = input("Select your dish: ")
#                 if dish in Swiggy.menu:
#                     ordered.append(dish)
#                     a = Swiggy.menu.index(dish)
#                     b = Swiggy.price[a]
#                     amount += b
#                     count += 1
#                 else:
#                     print("Your food is not in menu ")
#             elif select == "N" or "n":
#                 break
#             else:
#                 print("Print a valid statement ")
#     print()
#     print()

#     print("YOUR ORDERED ITEMS ARE: ")  # It tracks the ordered food
#     print()
#     for i in ordered:
#         print(i)

#     print()
#     print()

#     print("YOUR TOTAL AMOUNT: ", amount)  # Total amount is displayed
