def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    scores_copy = scores[:]
    scores_copy.sort()
    return scores_copy[-3:][::-1]
