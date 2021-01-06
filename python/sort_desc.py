data = {
    (1, 1): 32, (1, 2): 18, (1, 3): 5,
    (2, 1): 9, (2, 2): 64, (2, 3): 1,
    (3, 1): 96, (3, 2): 3, (3, 3): 27,
}

def change(data, j, k):
    """要素入れ替え関数
    m_y: data[(j, k)] ~ data[(3, 3)]間での最大値のAの縦軸インデックス
    m_x: data[(j, k)] ~ data[(3, 3)]間での最大値のAの横軸インデックス
    """
    m_y = j
    m_x = k
    x = k + 1
    y = j
    while y <= 3:
        while x <= 3:
            if data[(y, x)] > data[(m_y, m_x)]:
                m_y = y
                m_x = x
            x += 1
        x = 1
        y += 1
    w = data[(j, k)] 
    data[(j, k)] = data[(m_y, m_x)]
    data[(m_y, m_x)] = w

j = 1
while j <= 3:
    if j != 3:
        k = 1
        while k <= 3:
            change(data, j, k)
            k += 1
    else:
        k = 1
        while k <= 2:
            change(data, j, k)
            k += 1
    j += 1
print(data[(1,1)])
print(data)

