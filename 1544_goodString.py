def makeGood(s):
    l, r = 0, 1
    s_list = list(s)
    while l < len(s_list)-1:
        # print(len(s_list))
        if ord(s_list[l]) - ord(s_list[l+1]) == 32 and s_list[l].lower() == s_list[l+1].lower():
            # print(l)
            print(ord(s_list[l]) - ord(s_list[l+1]))
            s_list.pop(l)
            s_list.pop(l)
            l = 0
        else:
            l += 1
        # print(s_list)
    return "".join(s_list)

string = "Pp"
print(makeGood(string))