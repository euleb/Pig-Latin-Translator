import tkinter as tk

def piglatin(): 
    original_sentence = entry1.get()
    original_sentence = str.lower(original_sentence)
    original_word = original_sentence.split( )

    vowels = ['a','e','i','o','u']
    consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
    y_value = ["y"]
    translation = " "
    for word in original_word:
        if len(word) > 1:
            if word[1] in y_value: 
                if word[0] in vowels:
                    translation += word + 'ay' + ' '
                elif word[0] in consonants:
                    translation += word[1:] + word[0] + 'ay' + ' '
            elif word[0] in y_value:
                translation += word[1:] + word[0] + 'ay' + ' '
            elif word[0] in vowels:
                translation += word + 'ay' + ' '
            elif word[0] in consonants:
                translation += word[1:] + word[0] + 'ay' + ' '
        else:
            if word[0] in y_value:
                translation += word[1:] + word[0] + 'ay' + ' '
            elif word[0] in vowels:
                translation += word + 'ay' + ' '
            elif word[0] in consonants:
                translation += word[1:] + word[0] + 'ay' + ' '
    
   
    result_label.config(text =f'{translation}')

root = tk.Tk()
root.title("Pig Latin Translator")

title_text = "- Pig Latin Translator -"
title_label = tk.Label(text=title_text, bg="#585b67", fg="white", font="Courier")
title_label.pack(pady=10)
title_label.pack(padx=5)

question_frame = tk.Frame(root)
question_frame.pack(pady=10)

tk.Label(question_frame, text='Enter Text:', fg="#585b67").grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(question_frame)
entry1.grid(row=1, column=0, padx=10, pady=10)
calculate_button = tk.Button(text='Translate', command=piglatin, fg="#b0b1b8", bg="#585b67")
calculate_button.pack(pady=10)

tk.Label(question_frame, text='Pig Latin:', fg="#585b67").grid(row=0, column=1, padx=5, pady=5)
result_label = tk.Label(question_frame)
result_label.grid(row=1, column=1, padx=10, pady=10)

intro_text = "Pig Latin adds a fun twist to regular English. There are a few rules, but essentially\nthe first letter of a word gets taken and moved to the end with an ay sound.\nFor example, the word 'cat' would become 'at-cay'.\n-- Input a sentence to translate into Pig Latin! --"
intro_label = tk.Label(text=intro_text, bg="#585b67", fg="white")
intro_label.pack(pady=10)
intro_label.pack(padx=5)

root.mainloop()
