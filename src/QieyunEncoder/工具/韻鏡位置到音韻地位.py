# -*- coding: utf-8 -*-

'''
將韻鏡位置轉換爲音韻地位。
'''

from ..音韻地位 import 音韻地位
from ..韻鏡位置 import 韻鏡位置
from ..常量 import 常量


def 韻鏡位置到音韻地位(當前韻鏡位置: 韻鏡位置) -> 音韻地位:
    '''
    Test

    ```python
    >>> 韻鏡位置到音韻地位(韻鏡位置('幫', None, '三', '凡', '入')) == 音韻地位.from描述('幫三凡入')
    True
    ```
    '''
    韻鏡母號 = 當前韻鏡位置.韻鏡母號
    韻鏡母 = 當前韻鏡位置.最簡韻鏡母
    韻鏡開合 = 當前韻鏡位置.韻鏡開合
    韻鏡等 = 當前韻鏡位置.韻鏡等
    韻 = 當前韻鏡位置.韻
    聲 = 當前韻鏡位置.聲

    if 韻 in 常量.一三等韻:
        切韻等 = '一' if 韻鏡等 == '一' else '三'
    elif 韻 in 常量.二三等韻:
        切韻等 = '二' if 韻鏡等 == '二' else '三'  # TODO: 生
    else:
        切韻等 = None

    if 0 <= 韻鏡母號 < 4:  # 幫非組
        切韻母 = '幫滂並明'[韻鏡母號]
    elif 12 <= 韻鏡母號 < 17:  # 齒音
        if 韻鏡等 in '一四':
            切韻母 = '精清從心邪'[韻鏡母號 - 12]
        elif 韻鏡等 in '三':
            切韻母 = '章昌船書常'[韻鏡母號 - 12]  # TODO: 常船
        else:
            切韻母 = '莊初崇生俟'[韻鏡母號 - 12]
    elif 韻鏡母號 == 20:  # 喻母
        切韻母 = '云' if 韻鏡等 == '三' else '以'
    else:
        切韻母 = 韻鏡母

    if 切韻母 in '幫滂並明':
        切韻開合 = None
    else:
        切韻開合 = 韻鏡開合

    if 切韻母 not in 常量.重紐母 or 韻 not in 常量.重紐韻:
        重紐 = ''
    elif 韻鏡等 == '三':
        重紐 = 'B'
    else:
        重紐 = 'A'

    描述 = 切韻母 + (切韻開合 or '') + (切韻等 or '') + (重紐 or '') + 韻 + 聲
    return 音韻地位.from描述(描述)
