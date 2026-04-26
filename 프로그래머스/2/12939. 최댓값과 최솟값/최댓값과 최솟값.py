def solution(s):
    nums = sorted(list(map(int, s.split())))
    # return ' '.join((str(nums[0]), str(nums[-1])))
    return ' '.join(map(str, (nums[0], nums[-1])))