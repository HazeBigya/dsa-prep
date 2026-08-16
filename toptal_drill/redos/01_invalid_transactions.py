from collections import defaultdict


def invalid_transactions(transactions):
    transaction_dict = defaultdict(list)

    for t in transactions:
        name, time, amount, city = t.split(",")
        transaction_dict[name].append(
            {
                "name": name,
                "time": int(time),
                "amount": int(amount),
                "city": city,
                "t": t,
            }
        )

    invalid = set()

    for name, tnx in transaction_dict.items():
        for current in tnx:
            if current["amount"] > 1000:
                invalid.add(current["t"])
                continue

            for other in tnx:
                if (
                    other["city"] != current["city"]
                    and abs(other["time"] - current["time"]) <= 60
                ):
                    invalid.add(other["t"])
                    break

    return list(invalid)


transactions = [
    "alice,20,800,mtv",
    "alice,50,100,beijing",
    "bob,50,1200,mtv",
    "alice,90,100,mtv",
    "carol,10,50,nyc",
]

print("The invlaid transactions are: ", invalid_transactions(transactions))
