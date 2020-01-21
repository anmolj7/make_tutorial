from matplotlib import pyplot as plt
from collections import Counter


def main():
    with open('sample_data.txt') as f:
        data = f.read().split('\n') #It's actually better than
        # f.readlines because f.readlines leaves \n after every line.
        data = [line for line in data if len(line)]
    data = list(map(int, data)) #Changing the entire list's elements to list
    freq = dict(Counter(data))

    freq = sorted(freq.items())

    plt.pie([x[1] for x in freq], labels=[str(x[0]) for x in freq], autopct='%1.f%%', shadow=True)
    plt.title(f"Frequency Distriubution Of {len(data)} Numbers")
    plt.ylabel('Frequency')
    plt.xlabel('Number')
    plt.show()


if __name__ == "__main__":
    main()