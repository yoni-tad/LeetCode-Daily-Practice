from collections import defaultdict


class Trie:
    def __init__(self):
        self.children = {}
        self.delete = False

    def add(self, word):
        current = self
        for c in word:
            if c in current.children: current = current.children[c]
            else: current.children[c] = Trie()

def deleteDuplicateFolder():
    paths = [["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]] #[["d"],["d","a"]]
    root = Trie()
    for path in sorted(paths):
        root.add(path)

    def serialize(a):
        if not a.children: return ""
        
        s = []
        for folder, child in a.children.items():
            s.append(folder + '(' + serialize(child) + ')')
        key = "".join(s)
        seen[key].append(a)
        return key
    
    seen = defaultdict(list)
    serialize(root)

    for nodes in seen.values():
        if len(nodes) >= 2:
            for node in nodes: node.delete = True

    def dfs(root, path):
        for folder, child in root.children.items():
            if not child.delete:
                current = path + [folder]
                res.append(current)
                dfs(child, current)

    res = []
    dfs(root, [])
    return res


print(deleteDuplicateFolder())