import tkinter
import requests
import html

response = requests.get("https://opentdb.com/api.php?amount=50&type=boolean")
data = response.json()["results"]

questions = []
for item in data:
    questions.append(html.unescape(item["question"]))
    questions.append(item["correct_answer"])
# questions_dict = {}
# for i in range(0, len(questions), 2):
#     questions_dict[questions[i]] = questions[i + 1]
# print(questions_dict)

score = 0
q_list_index = 0
print(len(questions))


def select_true():
    global score, q_list_index
    if questions[q_list_index + 1] == "True":
        score += 1
        questions.remove(questions[q_list_index])
        questions.remove(questions[q_list_index])
        print(questions)
        quiz_label.config(text=questions[q_list_index])
        score_label.config(text=f"Score: {score}")
    else:
        q_list_index += 2
        quiz_label.config(text=questions[q_list_index])
        score_label.config(text=f"Score: {score}")


def select_false():
    global score, q_list_index
    if questions[q_list_index + 1] == "False":
        score += 1
        questions.remove(questions[q_list_index])
        questions.remove(questions[q_list_index])
        print(questions)
        quiz_label.config(text=questions[q_list_index])
        score_label.config(text=f"Score: {score}")
    else:
        q_list_index += 2
        quiz_label.config(text=questions[q_list_index])
        score_label.config(text=f"Score: {score}")


window = tkinter.Tk()
window.title("Quizzler.me")
window.minsize(400, 600)
canvas = tkinter.Canvas(width=300, height=310, bg="white")
canvas.place(x=48, y=110)

quiz_label = tkinter.Label(text="Quiz question will be displayed here What if now I am a big text who doesnt car e about anything",
                           font=("Ubuntu", 20), wraplength=250, bg="white", fg="black")
quiz_label.place(x=85, y=140)

score_label = tkinter.Label(text=f"Score: {score}", font=("Ubuntu", 20))
score_label.place(x=260, y=60)

true_image = tkinter.PhotoImage(file="images/true.png")
false_image = tkinter.PhotoImage(file="images/false.png")

true_button = tkinter.Button(image=true_image, command=select_true)  # Add command later
true_button.place(x=245, y=435)
false_button = tkinter.Button(image=false_image, command=select_false)  # Add command later
false_button.place(x=48, y=435)

quiz_label.config(text=questions[0])

window.mainloop()
