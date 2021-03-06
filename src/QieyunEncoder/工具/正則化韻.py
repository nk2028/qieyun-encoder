# -*- coding: utf-8 -*-

'''
將切韻系韻書的韻目轉換爲韻。
'''

_非標準韻表 = [
    '東董蕫送屋',
    '冬湩宋沃𣵽',
    '鍾腫用燭',
    '江講絳覺',
    '支紙寘',
    '脂旨至',
    '之止志',
    '微尾未',
    '魚語御',
    '虞麌噳遇',
    '模姥暮莫',
    '齊薺霽',
    '佳蟹卦',
    '皆駭怪',
    '灰賄隊',
    '咍海代',
    '眞諄軫準震稕質術',
    '臻𧤛櫬櫛',
    '文吻問物勿',
    '欣隱焮迄',
    '元阮願月',
    '魂混慁圂沒䰟',
    '痕很恨麧',
    '寒旱翰曷桓緩換末',
    '桓緩換末',
    '刪𠜂潸諫鎋舝',
    '山產襇黠',
    '先銑霰屑㞕',
    '仙㒨獮𤣗線薛𧀼',
    '蕭篠筱嘯',
    '宵小笑霄𥬇',
    '肴爻巧效',
    '豪晧号',
    '歌戈哿果箇過',
    '麻馬禡',
    '陽養漾藥',
    '唐蕩宕鐸',
    '庚梗映敬陌',
    '耕耿諍麥',
    '清靜勁昔㫺',
    '青迥徑錫',
    '蒸拯抍證職',
    '登等嶝隥德',
    '尤有宥',
    '侯矦厚𠪀候𠊱',
    '幽黝幼',
    '侵寑沁緝寢',
    '覃𧟹感勘合',
    '談敢𠭖闞盍盇',
    '鹽琰豔驗葉',
    '添沾忝㮇栝怗帖',
    '咸豏陷洽',
    '銜檻鑑狎',
    '嚴儼釅㽉業',
    '凡范梵乏',
    '祭',
    '廢',
    '泰',
    '夬𡗒',
]

_標準韻映射表 = {非標準韻: 非標準韻們[0] for 非標準韻們 in _非標準韻表 for 非標準韻 in 非標準韻們}


def 正則化韻(韻: str):
    '''
    將切韻系韻書的韻目轉換爲韻。

    ```python
    >>> 正則化韻('物')
    '文'
    >>> 正則化韻('敬')
    '庚'
    >>> 正則化韻('東')
    '東'
    ```
    '''
    return _標準韻映射表[韻]
