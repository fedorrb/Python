folder = [ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py']
filename = 'hereiam.py'
#folder = ['C:', 'backup.log', 'ideas.txt']
#filename = 'ideas.txt'
#folder = [ 'D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', 'asd.txt', 'asd.bak', 'find.me.bak' ] ], 'hey.py']
#filename = 'asd.txt'
def file_search(folder, filename):
    path = folder[0]
    found = False
    for f in folder:
        if f == filename and type(f) == str:
            found = path + '/' + f
    if found == False:
        for f in folder:
            if type(f) == list:
                path = file_search(f, filename)
                if path != False:
                    found = folder[0] + '/' + path
                    break
    return found
#********************************************
def file_search1(folder, filename):
    if folder == filename:
        return filename
    else:
        if isinstance(folder, list):
            if folder[0] == filename:
                return filename
            for i in folder[1:]:
                path = file_search1(i, filename)
                if isinstance(path, str):
                    return folder[0] + '/' + path
            return False
        else:
            return False
#**************************************************

print file_search(folder, filename)
