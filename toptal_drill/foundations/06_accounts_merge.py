from collections import defaultdict


def accountsMerge(accounts):
    parent = {}  # email -> its boss email (arrow). own boss when parent[e] == e
    owner = {}  # email -> name

    # climb arrows UP until a box points to itself -> top boss
    def find(e):
        while parent[e] != e:
            e = parent[e]
        return e

    # fuse two islands: point e1's boss at e2's boss
    def union(e1, e2):
        parent[find(e1)] = find(e2)
        print(
            f"Inside Union: {e1, e2}: e1: {find(e1)}, e2: {find(e2)}, parent: {parent}"
        )

    # Phase A: register emails + union each account's emails to the first
    for account in accounts:
        name = account[0]
        first_email = account[1]
        for email in account[1:]:
            if email not in parent:
                parent[email] = email
            owner[email] = name
            print("Owner : ", owner)
            union(first_email, email)  # <-- the glue you were missing

    # Phase B: bucket emails by their FINAL top boss
    groups = defaultdict(list)
    print(groups)
    for email in parent:
        groups[find(email)].append(email)
    print(groups)

    # Phase C: format -> [name, ...sorted emails]
    result = []
    for boss, email in groups.items():
        result.append([owner[boss]] + sorted(email))
    return result


if __name__ == "__main__":
    # a1 = [
    #     ["John", "a@x.com", "b@x.com"],
    #     ["John", "b@x.com", "c@x.com"],
    #     ["Mary", "m@x.com"],
    # ]
    # print(accountsMerge(a1))
    # # -> [['John','a@x.com','b@x.com','c@x.com'], ['Mary','m@x.com']]

    # bridging case: third account fuses two already-separate islands
    # a2 = [["Jhon", "x@x", "a@x"], ["J", "x@x", "c@x"], ["J", "b@x", "c@x"]]
    # print(accountsMerge(a2))
    # # -> one merged account: a@x, b@x, c@x, x@x

    a3 = [
        ["Jhon", "a", "b"],
        ["Jhon", "c", "d"],
        ["Mary", "e", "f"],
        ["Jhon", "b", "c"],
    ]
    print(accountsMerge(a3))
