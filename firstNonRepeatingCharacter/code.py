def firstNotRepeatingCharacter(s):

    rep_dict = {}
    ind_dict = {}
    for i in range(len(s)):
        if s[i] in rep_dict:
            rep_dict[s[i]] += 1
        else:
            rep_dict[s[i]] = 1
            
        if s[i] not in ind_dict:
            ind_dict[s[i]] = i
            
    rep_lst = [k for (k,v) in rep_dict.items() if v == 1]
    if len(rep_lst) < 1:
        return '_'
    
    index_dict = dict([(k,v) for (k,v) in ind_dict.items() if k in rep_lst])
    min_ch = min(index_dict,key=index_dict.get)
    return min_ch 
            
