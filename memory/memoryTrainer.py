import tkinter as tk

def display_memory_sequence(display_items, questions, display_t, answer_t):
    display_root = tk.Tk()
    display_root.title("Memory Trainer")
    display_root.attributes('-fullscreen', True)

    # Create a canvas to hold the content (centered)
    canvas = tk.Canvas(display_root, bg="white")
    canvas.pack(fill=tk.BOTH, expand=True)

    rows = len(display_items)
    cols = len(display_items[0])

    # Create an inner frame to hold the grid and center it within the canvas
    inner_frame = tk.Frame(canvas, bg="white")
    inner_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Create and place labels for each item
    for r in range(rows):
        for c in range(cols):
            label = tk.Label(inner_frame, text=display_items[r][c])
            label.config(font=("Arial", 35, "bold"))
            label.config(bg="white", fg="black")
            label.grid(row=r, column=c, padx=25, pady=25)

    canvas.config(scrollregion=canvas.bbox(tk.ALL))

    def check_answers():
        score = 0

        question_root = tk.Tk()
        question_root.title("Memory Trainer - Questions")
        question_root.attributes('-fullscreen', True)
        display_root.destroy()

        answer_boxes = []
        radio_objects = []

        for i, (qa, choices) in enumerate(questions):
            # Display question
            question_label = tk.Label(question_root, text=qa[0], font=("Arial", 20))
            question_label.pack(padx=20, pady=10)

            radio_objects.append(question_label)

            # Create integer variable to store selection (0 for first choice, etc.)
            answer_box = tk.IntVar(question_root)
            answer_boxes.append(answer_box)

            # Display choices as radio buttons in a frame below the question
            answer_frame = tk.Frame(question_root)
            answer_frame.pack()

            # Pack radio buttons side-by-side within the answer frame
            for j, choice in enumerate(choices):
                radio_button = tk.Radiobutton(answer_frame, text=choice, variable=answer_box, value=choice)
                radio_button.pack(side=tk.LEFT, padx=20)  # Use side=LEFT for horizontal placement
                radio_objects.append(radio_button)

        def grade_answers():
            grade_root = tk.Tk()
            grade_root.title("Memory Trainer - Grade")
            grade_root.attributes('-fullscreen', True)

            nonlocal score
            for i, (qa, choices) in enumerate(questions):
                user_answer = answer_boxes[i].get()
                if str(user_answer) == str(qa[1]):
                    score += 1
                    result_text = "Correct!"
                    result_color = "green"
                else:
                    result_text = f"Incorrect. The answer is: {qa[1]}, your answer: {user_answer}"
                    result_color = "red"

                # Display result for each question
                result_label = tk.Label(grade_root, text=f"Question {i + 1}: {result_text}", font=("Arial", 15),
                                        fg=result_color)
                result_label.pack(padx=20, pady=10)

            # Display final score
            final_score_label = tk.Label(grade_root, text=f"Your final score: {score}/{len(questions)}",
                                         font=("Arial", 20))
            final_score_label.pack(padx=20, pady=20)

            # remove prev screen and its timers
            question_root.destroy()

            def replay_game():
                grade_root.destroy()
                display_memory_sequence(display_items, questions, display_t, answer_t)

            replay_button = tk.Button(grade_root, text="Replay", font=("Arial", 15), command=replay_game)
            replay_button.pack(pady=20)

            grade_root.mainloop()

        # Grade answers after a delay
        question_root.after(answer_t * 1000, grade_answers)

        grade_now_button = tk.Button(question_root, text="Grade now", font=("Arial", 15), command=grade_answers)
        grade_now_button.pack(pady=20)

        # Run the question window's event loop
        question_root.mainloop()

    display_root.after(display_t * 1000, check_answers)

    display_root.mainloop()