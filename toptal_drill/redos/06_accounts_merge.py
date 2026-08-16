from collections import defaultdict


def accounts_merge(accounts):
    parent = {}
    owner = {}

    def find(e):
        while parent[e] != e:
            e = parent[e]
        return e

    def union(e1, e2):
        parent[find(e1)] = find(e2)

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
        groups[find(email)].append(email)

    result = []
    for root, email in groups.items():
        result.append([owner[root]] + sorted(email))

    return result


accounts = [
    ["John", "a@x.com", "b@x.com"],
    ["John", "c@x.com", "d@x.com"],
    ["Mary", "m@x.com", "n@x.com"],
    ["John", "b@x.com", "c@x.com"],
]
print(accounts_merge(accounts))
