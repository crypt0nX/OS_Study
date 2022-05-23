import random


def LRU(page, address):
    print(address)
    print("LRU页面置换过程为:")
    result = []
    loss_page = 0
    sum = 0
    for item in address:
        if len(result) == page:
            for j in range(sum, len(address)):
                if address[j] in result:
                    print("no exchange")
                    print("第%i页" % j, end="")
                    p = result[result.index(address[j])]
                    del result[result.index(address[j])]
                    result.insert(0, p)
                    print(result)
                else:
                    del result[-1]
                    result.insert(0, address[j])
                    loss_page += 1
                    print("第%i页" % j, end="")
                    print(result)
            break
        elif item in result:
            print("no exchange")
            p = result[result.index(item)]
            del result[result.index(item)]
            result.insert(0, p)
            print("第%i页" % sum, end="")
            print(result)
            sum += 1
        else:
            result.insert(0, item)
            loss_page += 1
            print("第%i页" % sum, end="")
            print(result)
            sum += 1
    result_page = float((loss_page) / len(address))
    print("LRU缺页率为：%.2f" % result_page)


if __name__ == '__main__':
    arr = []
    number1 = int(input("请输入页面长度"))
    for i in range(number1):
        arr.append(random.randint(1, number1))
    print(arr)

    number = int(input("请输入物理块数"))
    LRU(number, arr)
