def isomorphic_strings(s, t):
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for cs, ct in zip(s, t):
        if cs in s_to_t and s_to_t[cs] != ct:
            return False
        if ct in t_to_s and t_to_s[ct] != cs:
            return False

        s_to_t[cs] = ct
        t_to_s[ct] = cs

    return True


def isomorphic_strings_set(s, t):
    if len(s) != len(t):
        return False

    s_to_t = {}
    used = set()

    for cs, ct in zip(s, t):
        if cs in s_to_t:
            if s_to_t[cs] != ct:
                return False
        else:
            if ct in used:
                return False
            s_to_t[cs] = ct
            used.add(ct)

    return True


s = "carry"
t = "marie"

print("The stringss are s & t Isomorpic?: ", isomorphic_strings(s, t))
