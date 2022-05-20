import argparse

def cli_parser():
    parser = argparse.ArgumentParser(description='Task4')
    parser.add_argument('path_to_file', help='path_to_file')
    return parser.parse_args()


def parse_txt(file):
    numbers = []
    with open(file, 'r') as f2:
        while True:
            line = f2.readline().strip()
            if line:
                numbers.append(int(line.split('\n')[0]))
            if not line:
                break
    return numbers


def task4_run(nums):
    nums.sort()
    mid = len(nums) // 2
    res = 0
    for n in nums:
        res += abs(n - nums[mid])
    return res


def main():
    namespace = cli_parser()
    massiv = parse_txt(namespace.path_to_file)
    result = task4_run(massiv)
    print(result)


if __name__ == '__main__':
    main()