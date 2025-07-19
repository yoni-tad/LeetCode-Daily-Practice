def removeSubFolders():
    folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"] #["/a","/c/d","/c/f"]
    folder.sort()

    res = []
    for i in folder:
        if res and i.startswith(res[-1] + '/'): continue
        else: res.append(i)

    return res

print(removeSubFolders())