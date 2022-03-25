def pig_it(s):
    B = []
    z = list(s)
    #ВЫТАСКИВАЕМ ПЕРВУЮ БУКВУ СЛОВ
    B.append(z[0])
    del z[0]
    count = -1
    for i in z:
        count += 1
        if(z[count] !=' '):
            continue
        else:
            if(z[count+1]!= '!' and z[count+1]!= '.' and z[count+1]!= '?'):
                B.append(z[count+1])
                del z[count+1]
                continue

    #ДОБАВЛЯЕМ К НИМ "ay"
    dlB = len(B)
    while dlB > 0:
        dlB -= 1
        B[dlB] = B[dlB] + 'ay'
    #ЗАКИДЫВАЕМ В ОБЩИЙ СПИСОК ИЗМЕНЁННЫЕ БУКВЫ В КОНЕЦ СЛОВА, ИЗ КОТОРОГО ОНИ БЫЛО ВЗЯТЫ
    c = -1
    dlon = len(z)
    cB = 0
    for q in z:
        c += 1
        if(z[c]!= ' ' and (c+1 != dlon)):
            continue
        elif(z[c] == ' ' or (c+1 == dlon)):
            if(z[c] == ' '):
                z[c] = B[cB]
                cB += 1
                continue
            elif((c+1 == dlon) and (z[c] != '!' and z[c] != '.' and z[c] != '?')):
                z.append(B[cB])
                cB += 1
                continue
    #ДОБАВЛЯЕМ ПРОБЕЛЫ
    dlon2 = len(z)
    cc = -1
    for p in z:
        cc += 1
        if('ay' in z[cc]):
            if((cc+1 != dlon2)):
                z[cc] = z[cc] + ' '
                continue

    stroka = "".join(z)
    return stroka
m = pig_it("Quis custodiet ipsos custodes ?")
print(m)
