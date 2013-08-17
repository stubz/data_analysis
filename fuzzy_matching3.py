#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import re
import unicodedata

if __name__ == '__main__':
    r = re.compile(ur'([一二三四五六七八九十]+|[丁-龠]+|[ぁ-ん][ぁ-んー～゛゜]*|[ァ-ヶ][ァ-ヶー～゛゜]*|[0-9a-z][0-9a-z_\-]*)', re.UNICODE)
    k = re.compile(ur'[一-龠]', re.UNICODE)
    subject = u"ｽｹｼﾞｭｰﾙが切迫していたので、１４時に貴社の記者が汽車で帰社した。"
    subject = unicodedata.normalize('NFKC', subject).lower()
    words = r.findall(subject)
    words = [word for word in words if len(word) > 1 or k.search(word)]
    for x in words:
        print x,
