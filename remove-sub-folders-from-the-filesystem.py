def removeSubFolders():
    folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"] #["/a","/c/d","/c/f"]
    folder.sort()

    folder_split = [x.split('/') for x in folder]
    res = []

    # for i in range(len(folder_split)):
    #     for j in range(i, len(folder_split)):
    #         if not set(folder_split[i]).issubset(set(folder_split[j])):
    #             res.append(folder_split[j])
    #             # print(folder_split[j])

    for i in folder:
        if res and i.startswith(res[-1] + '/'): continue
        else: res.append(i)

                

    a = ['', 'c', 'd']
    b = ['', 'c', 'f', 'e']

    r = set(a).issubset(set(b))
    print(r)


    return res

print(removeSubFolders())