import tkinter as tk
from tkinter import filedialog
win = tk.Tk()

def browse_command():
    global file_path
    file_path = filedialog.askopenfilename()
    file_path_copy = file_path
    file_entry.delete(0, 'end')
    file_entry.insert(0,file_path)

def export_command():
    global file_path
    out_file = out_entry.get()
    out_file_sp = out_file.split('.')
    out_file_new = ''
    for counter in out_file_sp[0:len(out_file_sp)-1]:
        out_file_new = out_file_new + counter
    new_path = file_path.split('/')
    out_path = ''
    for counter in new_path[0:len(new_path)-1]:
        out_path = out_path + counter + '/'
    
    out_path_copy = out_path
    in_file = new_path[len(new_path)-1]
    in_file_sp = in_file.split('.')
    in_file_new = ''
    for counter in in_file_sp[0:len(in_file_sp)-1]:
        in_file_new = in_file_new + counter

    out_path = out_path + out_file_new
    import os
    os.system('libreoffice --headless --convert-to pdf '+file_path)
    os.system('mv '+out_path_copy + in_file_new +'.pdf '+out_path+'.pdf')

file_path = ''
label_info = tk.Label(win,text = 'PDF Dönüştürme Programı', font = 'Times 16')
browse_button = tk.Button(win,text = 'Dosya Seç',command = browse_command)
file_entry = tk.Entry(win,width = 50)
label_out = tk.Label(win,text = 'Çıktı Dosya Adı:')
out_entry = tk.Entry(win,width = 20)
out_entry.insert(0,'Output_file.pdf')
export_button = tk.Button(win,text = 'Dönüştür',command = export_command)

label_info.grid(row = 0, column = 0, columnspan = 2)
browse_button.grid(row = 1, column = 0)
file_entry.grid(row = 1, column = 1)
label_out.grid(row = 2, column = 0)
out_entry.grid(row = 2, column = 1,sticky = 'W')
export_button.grid(row = 3, column = 1, columnspan = 2)

win.mainloop()