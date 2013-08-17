#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import unicodedata

if __name__ == '__main__':
    subject = u"ｽｹｼﾞｭｰﾙがA切迫していたので、１４時に貴社の記者が汽車で帰社した。"
    subject = unicodedata.normalize('NFKC', subject).lower()
    print subject
