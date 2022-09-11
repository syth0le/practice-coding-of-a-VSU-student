class Field:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.up = None
        self.right = None
        self.down = None

    def __repr__(self):
        return self.value


def func(fields, n, m):
    result = ''
    for i in range(n):
        for j in range(m):
            if fields[i][j] == '.':
                continue
            if fields[i][j] == '*':



    return result


t = int(input())
results = []
for i in range(t):
    n, m = list(map(int, input().split()))
    fields = []
    for i in range(n):
        temp = input().split()
        fields.append(temp)
    for i in range(n):
        for j in range(m):
            if fields[i][j] == '*':
                field = Field('*')
                # if i in range(n) and j in range(m):
                if fields[i+1][j] == '*':
                    field.down = F

        temp = [Field(i) for i in input().split()]
        fields.append(temp)
    print(fields)
    # answer = func(fields, n, m)
    # results.append(answer)

for i in results:
    print(i)
