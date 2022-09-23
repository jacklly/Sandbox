def main():
    score = 0
    score = score_getter(score)
    if score > 100 or score < 0:
        print("Invalid score")
    elif score >= 90:
        print("Excellent score.")
    elif score >= 50:
        print("Passable score")
    else:
        print("Bad score")


def score_getter(score):
    score = int(input("Enter score: "))
    return score


main()
