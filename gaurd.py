fraud_words = ["Free", "lottery", "sbi-login" "bit.ly", "tinyurl"]

link = input("Link paste karo:")

fraud_hai = False
for word in fraud_words:
    if word in link.lower():
        fraud_hai = True

if fraud_hai:
    print("FRAUD HAI -Click mat karna bhai!")
else:
    print("Safe lag raha hai")            