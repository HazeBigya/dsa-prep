from collections import defaultdict


def invalid_transactions(transactions):
    transactions_dict = defaultdict(list)

    for t in transactions:
        name, time, amount, city = t.split(",")
        transactions_dict[name].append(
            {
                "name": name,
                "time": int(time),
                "amount": int(amount),
                "city": city,
                "t": t,
            }
        )

    invlaid = set()

    for name, tnx in transactions_dict.items():
        for curr in tnx:
            if curr["amount"] > 1000:
                invlaid.add(curr["t"])
                continue

            for oth in tnx:
                if curr["city"] != oth["city"] and abs(curr["time"] - oth["time"]):
                    invlaid.add(oth["t"])
                    break

    return list(invlaid)


transactions = [
    "alice,20,800,mtv",
    "alice,50,100,beijing",
    "bob,50,1200,mtv",
    "alice,90,100,mtv",
    "carol,10,50,nyc",
]

print("The invlaid transactions are: ", invalid_transactions(transactions))
