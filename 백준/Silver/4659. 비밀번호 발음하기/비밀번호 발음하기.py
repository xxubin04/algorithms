input = open(0).readline

def seq2(current_w):
    global cnt
    if (current_w == 'o' or current_w == 'e') and cnt == 1:
        cnt = 2
        return False
    else:
        return True

def seq3(current_w, prior_w):
    global prior, current, cnt
    if current == prior and current_w == prior_w:
        return seq2(current_w)
    elif current == prior and cnt < 2:
        prior = current
        cnt += 1
        return False
    elif current == prior and cnt == 2:
        return True
    else:
        prior = current
        cnt = 1
        return False

while (word := input().strip()) != "end":
    vowel_appear = False
    acceptance = 1
    for w in range(len(word)):
        if w == 0:
            prior_w = word[w]
            if word[w] in ['a', 'e', 'i', 'o', 'u']:
                vowel_appear = True
                prior = 0
            else:
                prior = 1
            cnt = 1
        else:
            if word[w] in ['a', 'e', 'i', 'o', 'u']:
                vowel_appear = True
                current = 0
            else:
                current = 1
            if seq3(word[w], prior_w):  # not acceptable
                acceptance *= 0
            prior_w = word[w]

    if vowel_appear and acceptance:  # acceptable과 not 분류 부분
        print(f"<{word}> is acceptable.")
    else:
        print(f"<{word}> is not acceptable.")