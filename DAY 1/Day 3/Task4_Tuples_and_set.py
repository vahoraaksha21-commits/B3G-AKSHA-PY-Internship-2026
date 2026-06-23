subscribers={"aksha@gmail.com","aafiya@gmail.com","jiya@gmail.com"}
customers={"aafiya@gmail.com","jiya@gmail.com","ilma@gmail.com"}

never_purchased=subscribers-customers
never_subscribed=customers-subscribers

print("Subscribers Who never made a Purchase:")
print(never_purchased)
print("\nCustomers Who Purchased but never Subscribed:")
print(never_subscribed)