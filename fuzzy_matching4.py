#! /usr/bin/env python
# -*- coding: utf-8 -*-
## http://d.hatena.ne.jp/deb/20110526
## にあった、日本語の曖昧検索の事例
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import re
import unicodedata

haystack = [
    ur'ｽｹｼﾞｭｰﾙが切迫していたので、１４時に貴社の記者が汽車で帰社した。',
    ur'スケジュールの切迫により、１４時に御社の記者が汽車で帰社した。',
    ur'庭には二羽鶏がいる。',
    ur'予定通り、１４時に貴社の記者が汽車で帰社した。',
    ur'予定通り、１４時に貴社の記者が電車で帰社した。',
]

def build(subject, type):
    r = re.compile(ur'([一二三四五六七八九十]+|[丁-龠]+|[ぁ-ん][ぁ-んー～゛゜]*|[ァ-ヶ][ァ-ヶー～゛゜]*|[0-9a-z][0-9a-z_\-]*)', re.UNICODE)
    k = re.compile(ur'[一-龠]', re.UNICODE)
    h = re.compile(ur'[ぁ-んー～]', re.UNICODE)
    subject = unicodedata.normalize('NFKC', subject).lower()
    words = r.findall(subject)


    if type:
        result = [word for word in words if len(word) > 1 or k.search(word)]
    else:
        result = []
        for i, w in enumerate(words):
            if len(w) > 1 or k.search(w):
                result.append(w)
            elif i > 0 and (len(w) == 1 and h.search(w)):
                result.append(result.pop() + w)

    return result

def search(subject, database):
    # 簡易高速版 しかし配列順序が保持されない。
    # result = [(list(set(d) & set(subject)),i) for i, d in enumerate(database)]

    # 真面目に処理版
    result = []
    for i, d in enumerate(database):
        hit = []
        for s in subject:
            if s in d:
                hit.append(s)
        if hit:
            result.append((hit, i))
    return result

if __name__ == '__main__':
    print u'＊漢字でない一文字の単語は削除する方法'
    subject = build(ur"ｽｹｼﾞｭｰﾙが切迫していたので、１４時に貴社の記者が汽車で帰社した。", True)
    database = [build(v, True) for v in haystack]
    result = search(subject, database)
    for r in result:
            print haystack[r[1]]
            print ur'A', '->', ((len(r''.join(r[0]))*1.0) / (len(r''.join(subject))*1.0)) * 100.0, ur'%'
            print ur'B', '->', (len(r[0])*1.0) / (len(subject)*1.0) * 100.0, ur'%'
    
    print u'\n'
    
    print u'＊ひらがな一文字の単語を削除せず前の単語に結合する方法'
    subject = build(ur"ｽｹｼﾞｭｰﾙが切迫していたので、１４時に貴社の記者が汽車で帰社した。", False)
    database = [build(v, False) for v in haystack]
    result = search(subject, database)
    for r in result:
            print haystack[r[1]]
            print ur'A', '->', ((len(r''.join(r[0]))*1.0) / (len(r''.join(subject))*1.0)) * 100.0, ur'%'
            print ur'B', '->', (len(r[0])*1.0) / (len(subject)*1.0) * 100.0, ur'%'

