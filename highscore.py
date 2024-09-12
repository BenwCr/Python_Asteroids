from constants import MAX_HSENTRIES, HS_DOC

def is_highscore(score):
    highscore_doc = open_doc(HS_DOC)('read')
    lst_index = -1
    for entry in highscore_doc:
        lst_index += 1
        lst_entry = entry.split('/')
        if len(lst_entry) != 3 or score >= int(lst_entry[0]): #New HighScore to replace
            score_entry = lst_entry[0]
            return lst_index
    return -1


def highscore_update(index):
    pass


def open_doc(filePath=HS_DOC):
    def inner(doc_action,score=0,time=0,name='',index= -1):
        f = open(filePath)
        init_content = f.read().split('\n')[:MAX_HSENTRIES]
        f.close()
        if doc_action == 'write':
            if len(init_content) >= MAX_HSENTRIES:
                del init_content[MAX_HSENTRIES - 1]
            content = str(score) + '/' + str(time) + '/' + name.replace('/','')
            init_content.insert(index,content)
            new_doc = "\n".join(init_content)
            wf = open(filePath, 'w')
            wf.write(new_doc)
            wf.close()
            return new_doc

        return init_content
    return inner
    




