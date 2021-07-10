# -*- coding: utf-8 -*-

'''
將母轉換爲清濁。
'''

_清濁到母表 = (
    ('全清', '幫端知精心莊生章書見影曉'),
    ('次清', '滂透徹清初昌溪'),
    ('全濁', '並定澄從邪崇俟常船羣匣'),
    ('次濁', '明泥孃來日疑云以'),
)

_d母到清濁 = {母: 清濁 for 清濁, 母們 in _清濁到母表 for 母 in 母們}


def 母到清濁(母: str):
    '''
    將母轉換爲清濁。

    ```python
    >>> 母到清濁('端')
    '全清'
    >>> 母到清濁('以')
    '次濁'
    ```
    '''
    return _d母到清濁[母]
