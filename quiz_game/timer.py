import time


def countdown(seconds, answer_continer):
    for _ in range(seconds):
        time.sleep(1)

    if answer_continer["answer"] is not None:
        return
    print("⌛️ Time's up!!")
    answer_continer["answer"] = ""

