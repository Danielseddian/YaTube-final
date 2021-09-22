import requests
import asyncio


SOURCE_URL = (
    "https://raw.githubusercontent.com/avito-tech/"
    "python-trainee-assignment/main/matrix.txt"
)


async def get_matrix(url=SOURCE_URL):
    table = requests.get(url).text
    matrix = []
    count = 0
    for line in table.split("\n"):
        if count % 2 & len(line) > 0:
            matrix.append(list(map(int, line.replace("|", "").split())))
        count += 1
    result = []
    left, right, up, down = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
    index_0, index_1 = -1, 0
    while down > up or right > left:
        while index_0 < down:
            index_0 += 1
            result.append(matrix[index_0][index_1])
        left += 1
        while index_1 < right:
            index_1 += 1
            result.append(matrix[index_0][index_1])
        down -= 1
        while index_0 > up:
            index_0 -= 1
            result.append(matrix[index_0][index_1])
        right -= 1
        while index_1 > left:
            index_1 -= 1
            result.append(matrix[index_0][index_1])
        up += 1
    return result


if __name__ == "__main__":
    print(asyncio.run(get_matrix()))
