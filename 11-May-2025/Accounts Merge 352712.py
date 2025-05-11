# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = [i for i in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        email_to_index = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_index:
                    union(i, email_to_index[email])
                else:
                    email_to_index[email] = i

        index_to_emails = defaultdict(set)

        for email, idx in email_to_index.items():
            root = find(idx)
            index_to_emails[root].add(email)

        res = []
        for idx, emails in index_to_emails.items():
            res.append([accounts[idx][0]] + sorted(emails))

        return res
