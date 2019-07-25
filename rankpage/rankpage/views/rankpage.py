from collections import defaultdict

from pyramid.httpexceptions import HTTPForbidden
from pyramid.view import view_config

from cornice import Service


# get rank info
chictr_info = Service(name='rank',
                    path='/{username}/rankinfo',
                    description='Get Rank info.')

_USERS_category = defaultdict(dict)
@chictr_info.get()
def get_info(request):
    """Returns the public information about a **user**.
    If the user does not exists, returns an empty dataset.
    """
    username = request.matchdict['username']
    return _USERS[username]


@chictr_info.post()
def set_info(request):
    """Set the public information for a **user**.
    You have to be that user, and *authenticated*.
    Returns *True* or *False*.
    """
    import codecs
    import random

    # 获得上传的文件，计算出macro_f1值
    # macrof1 = random.uniform(0, 1)

    # 将该条结果增添之结果记录文件results.txt
    data = request.json_body
    macrof1 = data["macrof1"]
    print(data)
    import os
    print(os.getcwd())
    with codecs.open("./rankpage/views/results.txt", "a+", encoding ="utf-8") as f1:
        if data["name"] and data["tfidf"] and data["size"] and data["epoch"] and data["batchsize"] and data["learningrate"] and macrof1:
            f1.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(data["name"], data["tfidf"], data["size"], data["epoch"], data["batchsize"], data["learningrate"], macrof1))

    # 读取结果记录文件results.txt, 获得所有结果，并按照macrof1值排序
    results = []
    with codecs.open("./rankpage/views/results.txt", "r", encoding ="utf-8") as f2:
        for line in f2:
            results.append(tuple(line.strip().split("\t")))

    rankinfo = sorted(results, key=lambda x: x[-1], reverse=True)
    rankinfo = [[i + 1] + list(rankinfo[i]) for i in range(len(rankinfo))]
    print(rankinfo)
    return rankinfo
