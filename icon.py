from tkinter import *
from tkinter import ttk
from tkinter import StringVar, messagebox
from PIL import Image, ImageTk
from tkinter import filedialog
import os


root = Tk()
root.geometry('500x650')
root.title('Icon Converter')
root.configure(bg = '#c2d6d6')



def browse():
    global opened_file
    global filename


    filetypes= (("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("icon files", "*.ico"))
    open_file = filedialog.askopenfilename(filetypes= filetypes, initialdir='C:', title='Choose an image', )
    filename = os.path.basename(open_file)
    fname.cget('text')
    fname.configure(text = (f"{filename}"))
    opened_file = Image.open(open_file)



    # Create a photoimage object of the image in the path
    resized_image = opened_file.resize((150,150))
    photo = ImageTk.PhotoImage(resized_image)
    label1 = Label(root, image = photo)
    label1.image = photo

    # Position image
    label1.place(relx=0.65, rely=0.12)
    

def convert():
    # Convert image to .ico and save it
    try:
        save = filedialog.asksaveasfilename(filetypes=[("icon files", "*.ico")])
        opened_file.save(f'{save}.ico')

        messagebox.showinfo('Success','Icon converted successfully!')
    except:
        messagebox.showerror('Error', 'Something went wrong!!!')
    

#creating the title label
selet_label = Label(root, text = 'ICON Converter',  bg='#c2d6d6', fg = 'black', font=("Courier", 20, 'bold'))
selet_label.place(relx = '0.25',rely = '0.03')

#creating the select image label
select_image  = Label(root,text = 'Select Image', bg='#c2d6d6', fg = 'black',  font=("Courier", 12, 'bold'))
select_image.place(relx = '0.05',rely = '0.15')

#browse description label
select_browse = Label(root, text='PNG, JPEG, GIF, ICO, etc. must be less than 4 Mb...', bg='#c2d6d6', fg = 'black', font=("Ariel", 8))
select_browse.place(relx = '0.05',rely = '0.19')

#browse button
browse_button = Button(root, text='Choose File', command=browse, font=("Courier", 10), relief = 'groove')
browse_button.place(relx='0.05', rely='0.23')

#file name holder label
fname = Label(root, font=("Courier", 10), text = 'No file chosen' , fg = "black", bg ='#c2d6d6')
fname.place(relx='0.28', rely='0.24')



#creating the select image label
save_image  = Label(root,text = 'Convert Image', bg='#c2d6d6', fg = 'black',  font=("Courier", 12, 'bold'))
save_image.place(relx = '0.05',rely = '0.35')

#browse description label
save_desc = Label(root, text='Image will be saved as Alluvium.ico', bg='#c2d6d6', fg = 'black', font=("Ariel", 8))
save_desc.place(relx = '0.05',rely = '0.38')

convert_button = Button(root, text='Convert', command=convert, font=("Arial", 10), relief = 'groove')
convert_button.place(relx=0.05, rely=0.42)


root.mainloop()
