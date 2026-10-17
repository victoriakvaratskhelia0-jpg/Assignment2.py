import re
text = input("Minda 3cali bileti, bileti  15 lari: ")
numbers = re.findall(r"\d+", text)
try:
 tickets = int(numbers[0])
 money = int(numbers[1])
 total_price = tickets * 15
 if tickets <= 0 :
    raise ValueError("ბილეთების რაოდენობა უნდა იყოს მინიმუმ 1")
 if (money < tickets * 15):
    raise ValueError("თანხა არ არის საკმარისი")
 price_per_ticket = money / tickets
except (ZeroDivisionError,ValueError) :
    print("თანხა არ არის საკმარისი")
except IndexError:
    print("Error: Please provide both the number of tickets and the totalmoney.")
else:
   print(f"თითოეული ბილეთის ფასი არის {price_per_ticket} ლარი")
   change = money - total_price
   print(f"ოპერაცია წარმატებულია, დარჩენილი თანხა არის {change:.2f} ლარი")
finally:
   print("[სისტემა]:ტრანზაქციის მცდელობა დასრულდა")

