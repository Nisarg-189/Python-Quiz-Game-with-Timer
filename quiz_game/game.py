import threading
from timer import countdown

def ask_question(q, time_limit=10):
    answer_container = {"answer": None}

    print("\n" + q["question"])
    
    # PRINT ALL OPTIONS PROPERLY
    for opt in q["options"]:
        print(opt)

    # Timer thread
    t = threading.Thread(target=countdown, args=(time_limit, answer_container))
    t.start()

    answer_container["answer"] = input("\nYour answer: ")
    t.join()

    if answer_container["answer"].lower() == q["answer"].lower():
        print("✅ Correct!")
        return True
    else:
        print(f"❌ Wrong! Correct answer: {q['answer'].upper()}")
        return False

        



def run_quiz(questions):

    print("====== Welcom to the Quiz Game ======")
    print("You have 10 seconds to answer each question \n")

    score = 0

    for q in questions:
        if ask_question(q):
            score += 1

    print("===== Quiz Finished =====")
    print(f"\n Your score : {score}/ {len(questions)}")



