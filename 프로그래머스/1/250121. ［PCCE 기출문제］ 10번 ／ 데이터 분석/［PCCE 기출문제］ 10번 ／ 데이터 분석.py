def solution(data, ext, val_ext, sort_by):
    answer = []
    extli=["code","date","maximum","remain"]
    extindex=extli.index(ext)
    dataindex=extli.index(sort_by)
    for i in data:
        if i[extindex]<val_ext:
            answer.append(i)
    answer= sorted(answer, key= lambda x:x[dataindex])

    return answer