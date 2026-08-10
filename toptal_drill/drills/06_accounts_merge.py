"""
Toptal Top-20 Target #6 — Accounts Merge
Frequency: 82%  |  Difficulty: Medium
Pattern: Union-Find (or DFS on a graph of emails)

STATUS: TODO (roadmap stub — solve from scratch, out loud, then cold-redo)
Foundation: foundations/08_number_of_islands.py (flood/connectivity)

Problem:
  Given accounts[i] = [name, email1, email2, ...], merge accounts that
  share ANY email (same person). Return merged accounts, each as
  [name, sorted_email1, sorted_email2, ...]. Two accounts with the same
  name are only merged if they share an email.

Approach:
  1. Model emails as nodes; emails in the same account are connected.
  2. Union all emails within each account (union-find), keep email->name.
  3. Group emails by their root parent, sort each group, prepend the name.

Example:
  accounts = [["John","a@x.com","b@x.com"],["John","b@x.com","c@x.com"],["Mary","m@x.com"]]
  # -> [["John","a@x.com","b@x.com","c@x.com"],["Mary","m@x.com"]]
"""


def accountsMerge(accounts):
    # TODO: your solution here
    pass
