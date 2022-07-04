# Import modules
    
# Practice5: array dict
# table = {}
# for i in range(0, 5):
#     key = str(input("請輸入一串字："))
#     value = int(input("請輸入數字："))
#     table[key] = value
    
# print(table)

singer = {}

for i in range(0, 5):
    key = str(input("請輸入歌手："))
    value = int(input("請輸入分數："))
    singer[key] = value
    
for i in range(0, 5):
    searchName = str(input("請輸入歌手："))
    if singer.get(searchName, '404') == '404':
        print("此人並未參賽")
    else:
        print("歌手名字：", searchName, end=' ')
        print("歌手分數：", singer[searchName])