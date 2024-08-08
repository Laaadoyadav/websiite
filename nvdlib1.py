import tkinter as tk
import nvdlib

def on_submit():
    # Retrieve the text from the entry field
    entered_text = entry.get()
    if (entered_text.startswith('CVE') == True or entered_text.startswith('cve')== True):
        r = nvdlib.searchCVE(cveId= entered_text )[0]
##        strg = r.v31severity + ' - ' + str(r.v31score)
##        desc = str(r.descriptions[0].value)
##        score = str(r.v31vector)
        full = f"{entered_text}\n\n{str(r.descriptions[0].value)}\n\n{r.v31severity}\n{str(r.v31score)}{' - '}{str(r.v31vector)}"
        print(full)
        output_text.delete(1.0, tk.END)  # Clear previous text
        
        output_text.insert(tk.END, full)
##        output_text.insert(tk.END, strg)
##        output_text.insert(tk.END, score)
    else:
        output_text.delete(1.0, tk.END)  # Clear previous text
        output_text.insert(tk.END, entered_text)  # Insert new text
        
def copy_to_clipboard():
    # Retrieve text from the text widget
    text_to_copy = output_text.get(1.0, tk.END).strip()
    
    # Clear the clipboard and append the text
    root.clipboard_clear()
    root.clipboard_append(text_to_copy)
    root.update()  # Update the root window to ensure clipboard is updated

# Create the main application window
root = tk.Tk()
root.title("CVE search")
root.configure(bg='DeepSkyBlue2')
# Create and place a label
text_label=tk.Label(root, text="Enter CVE ID:", bg='turquoise1',width=15)
text_label.pack(padx=15, pady=5)
# Create and place an entry field
entry = tk.Entry(root, selectbackground="lightblue", selectforeground="black", width=70)
entry.pack(padx=10, pady=5)

# Create and place a submit button
submit_button = tk.Button(root, text="Submit",bg='turquoise1', command=on_submit)
submit_button.pack(padx=10, pady=10)

# Create and place an output label
output_text = tk.Text(root, height=5, width=50, wrap=tk.WORD)
output_text.pack(padx=10, pady=10)

# Create and place a copy button
copy_button = tk.Button(root,bg='turquoise1', text="Copy", command=copy_to_clipboard)
copy_button.pack(padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
