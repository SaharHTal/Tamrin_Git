import re


def linear_search(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return 0


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if int(left[i]) < int(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(nums_str):
    if len(nums_str) <= 1:
        return nums_str
    mid = len(nums_str) // 2
    left_half = nums_str[:mid]
    right_half = nums_str[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return "".join(merge(left_half, right_half))


class MrCrabs:
    def __init__(self, primary_dna):
        self.primary_dna = primary_dna
        self.ten_characters = self.primary_dna[:10]
        self.primary_dna = self.primary_dna + self.ten_characters
        self.new_dna = re.sub(r"tt", "o", self.primary_dna)

    def print_dna(self):
        print(self.new_dna)


class SpongeBob(MrCrabs):
    def __init__(self, primary_dna):
        super().__init__(primary_dna)
        self.sort_length = merge_sort(str(len(self.new_dna)))

    def print_dna(self):
        print(self.sort_length)


class Squidward:
    def __init__(self, primary_dna):
        self.primary_dna = primary_dna
        self.new_dna = re.sub(r"(.)\1\1", "(0_0)", self.primary_dna)
        self.newer_dna = self.new_dna
        for i in range(len(self.primary_dna)):
            if self.primary_dna[i] == "x":
                self.newer_dna += str(i)
                break

    def print_dna(self):
        print(self.newer_dna)

x = input()
if re.findall(r"\Am", x):
    y = MrCrabs(x)
    y.print_dna()
elif re.findall(r"\Asb", x):
    y = SpongeBob(x)
    y.print_dna()
elif re.findall(r"\As", x):
    y = Squidward(x)
    y.print_dna()
elif re.findall(r"bs\Z", x):
    x = x[::-1]
    y = SpongeBob(x)
    y.print_dna()
elif re.findall(r"s\Z", x):
    x = x[::-1]
    y = Squidward(x)
    y.print_dna()
elif re.findall(r"m\Z", x):
    x = x[::-1]
    y = MrCrabs(x)
    y.print_dna()
else:
    print("invalid input")


