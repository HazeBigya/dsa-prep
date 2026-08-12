from collections import defaultdict


def accounts_merge(accounts):
    owner = {}
    parent = {}

    def find_boss(e):
        while parent[e] != e:
            e = parent[e]
        return e

    def union(e1, e2):
        parent[find_boss(e1)] = find_boss(e2)

    for account in accounts:
        name = account[0]
        first_email = account[1]
        for email in account[1:]:
            if email not in parent:
                parent[email] = email
            owner[email] = name
            union(first_email, email)

    groups = defaultdict(list)
    for email in parent:
        groups[find_boss(email)].append(email)

    result = []
    for boss, email in groups.items():
        result.append([owner[boss]] + sorted(email))
    print(result)


accounts = [
    ["John", "a@x.com", "b@x.com"],
    ["John", "c@x.com", "d@x.com"],
    ["Mary", "m@x.com", "n@x.com"],
    ["John", "b@x.com", "c@x.com"],
]
accounts_merge(accounts)
