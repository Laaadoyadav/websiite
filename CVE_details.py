import nvdlib
import tkinter
import xlsxwriter

import tkinter as tk
import nvdlib


def on_submit():
    workbook = xlsxwriter.Workbook('Example3.xlsx')
    worksheet = workbook.add_worksheet("My sheet")
    row = 0
    col = 0

    scores = [
            ['CVE', 'Description','Severity', 'CVSS Score', 'Vector'],
            ]
    entered_text = entry.get()
    cve_id = entered_text.split()
    cve_detail = [];
    for i in range (len(cve_id) ):
        cve = cve_id[i]
        if (cve.startswith('CVE') == True or cve.startswith('cve')):
            r = nvdlib.searchCVE(cveId= cve )[0]
            full = f"{cve}\n{str(r.descriptions[0].value)}\n{r.v31severity}\n{str(r.v31score)}\n{str(r.v31vector)}"
            components = full.split('\n')
            print(type(components))
            print(type(scores))
            scores.append(components)
    for a, b,c,d,e in (scores):
        worksheet.write(row, col, a)
        worksheet.write(row, col + 1, b)
        worksheet.write(row, col + 2, c)
        worksheet.write(row, col + 3, d)
        worksheet.write(row, col + 4, e)
        row += 1

    workbook.close()     

# Create the main application window
root = tk.Tk()
root.title("CVE search")
root.configure(bg='DeepSkyBlue2')
# Create and place a label
text_label=tk.Label(root, text="Enter CVE ID:", bg='turquoise1',width=70)
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

### Create and place a copy button
##copy_button = tk.Button(root,bg='turquoise1', text="Copy", command=copy_to_clipboard)
##copy_button.pack(padx=10, pady=10)

# Start the GUI event loop
root.mainloop()


