from collections import defaultdict


def invalid_transactions(transaction):
    dict = defaultdict(list)

    for t in transaction:
        name, time, amount, city = t.split(",")
        dict[name].append(
            {
                "name": name,
                "time": int(time),
                "amount": int(amount),
                "city": city,
                "t": t,
            }
        )

    invalid = set()

    for name, tnx in dict.items():
        for cur in tnx:
            if cur["amount"] > 1000:
                invalid.add(cur["t"])
                continue
            for other in tnx:
                if (
                    other["city"] != cur["city"]
                    and abs(other["time"] - cur["time"]) <= 60
                ):
                    invalid.add(cur["t"])
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
