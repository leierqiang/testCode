import os

abc = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"


def abc_all(s):
    res = ''
    for i in range(len(s)):
        for j in range(len(s)):
            for k in range(len(s)):
                for l in range(len(s)):
                    for m in range(len(s)):
                        s_2 = s[i] + s[j] + s[k] + s[l] + s[m]
                        res += s_2 +'.com' + '\r'  # 换行
                        # print(res)

    with open(r"E:\testCode\Python\testProject_1\data.txt",'w+') as f:
        f.write(res) 

if __name__ == "__main__":
    # abc_all(abc)
    abc_all(num)
