import tkinter as tk 
root=tk.Tk()
root.title("File Organizer")
root.geometry("400x250")

def show_input():
    user_input=entry.get()
    print("User input :",user_input)


label=tk.Label(root,text="Enter Folder Adrress")
label.pack(pady=10)

entry=tk.Entry(root,width=100)
entry.pack(pady=5)

button=tk.Button(root,text="Submit",command=show_input)
button.pack(pady=10)

root.mainloop()