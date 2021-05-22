from tkinter import *
from tkinter.font import Font
from list_predictor import AutocompleteEntry
from list_predictor import AutocompleteCombobox
from PIL import ImageTk, Image
from PIL import Image
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import pairwise_distances

class Application():
    def __init__(self, master):
        self.no = 0
        self.key = -1
        self.master = master
        self.master.title('movies')
        self.top = Frame(self.master, height=80, width=1536, bg='#5e615e')
        self.top.pack(side=TOP)
        self.fs = Frame(self.master, height=5, width=1536, bg='red')
        self.fs.pack()

        self.bottom = Frame(self.master, height=300, width=1536, bg='#2b2929')
        self.bottom.pack()

        self.temp1 = Frame(self.master,height = 260,width = 1536,bg = "#2b2929")
        self.temp1.pack()
        self.temp2 = Frame(self.master, height=150, width=1536, bg='#2b2929')
        self.temp2.pack()
        self.temp3 = Frame(self.master, height=5, width=1536, bg='red')
        self.temp3.pack()
        self.temp4= Frame(self.master, height=50, width=1536, bg='#5e615e')
        self.temp4.pack()


        self.my_font = Font(family='Ink Free', size=42, weight='bold')
        self.label = Label(self.top, text='Amazon Product Recommendation', bg='#5e615e', fg='#0696c2',font=self.my_font)
        self.label.place(x=400, y=10)
        my_font = Font(family='Ink Free', size=105, weight='bold')
        self.ads_label = Label(self.temp1, text="Amazon Top's Faishon", bg='#2b2929', fg='#f5f51d',font=my_font)
        self.ads_label.place(x=100, y=0)


        self.d = pd.read_csv("Preprocessed_tops_data.csv")
        self.entry_box(500,120,720,190)
    def Ml_model(self,doc_id):

        data = pd.read_pickle('pickles_16k_apperal_data_preprocessed')
        tfidf_title_vectorizer = TfidfVectorizer(min_df=0)
        tfidf_title_features = tfidf_title_vectorizer.fit_transform(data['title'])
        pairwise_dist = pairwise_distances(tfidf_title_features, tfidf_title_features[doc_id])
        indices = np.argsort(pairwise_dist.flatten())[0:20]
        pdists = np.sort(pairwise_dist.flatten())[0:20]
        df_indices = list(self.d.index[indices])
        self.asin = []
        self.title = []
        self.image = []
        for i in range(0, len(indices)):
            self.asin.append(self.d['asin'].loc[df_indices[i]])
            self.title.append(self.d['title'].loc[df_indices[i]])
            try:
                image = Image.open(f"16k_images/{self.d['asin'].loc[df_indices[i]]}.jpeg")
            except:
                image = Image.open("16k_images/not_available.jpg")
            new_image = image.resize((200, 225))
            self.image.append(new_image)

    def update_list(self):
        self.search_button.destroy()
        self.combo.destroy()
        self.temp1.destroy()
        self.temp2.destroy()
        self.temp3.destroy()
        self.temp4.destroy()
        self.ads_label.destroy()
        self.entry_box()
        myfont = Font(family='Ink Free', size=20, weight='bold')
        Label(self.bottom, text='Recommanded for you', font=myfont, bg='#2b2929', fg='#6dad86').place(x=15, y=200)

        self.canvas = Canvas(self.master, height=300, width=1536, bg='#2b2929')
        self.scroll_y = Scrollbar(self.master, orient="horizontal", command=self.canvas.xview, bg='#2b2929',troughcolor='#2b2929')
        self.frame = Frame(self.canvas, bg='red', width=1536)
        self.frame_label = Frame(self.canvas, bg='#2b2929', width=1536)

        self.fram = Frame(self.frame)
        ph = ImageTk.PhotoImage(self.image[1])
        self.fram = Frame(self.frame, height=100, width=200, bg='#2b2929', cursor='hand2')
        l1 = Label(self.fram, image=ph)
        l1.bind('<Button-1>', lambda a: self.get(key=1))
        l1.pack(side=LEFT, padx=10)
        self.fram.pack(side=LEFT)
        l1.image = ph
        self.fra = Frame(self.frame_label, height=60, width=200, bg='#2b2929')
        self.fra.pack(side=LEFT, padx=10)
        x = Label(self.fra, text=f'{self.title[1][:30]}...', width=30, fg='yellow', bg='#2b2929')
        x.place(x=0, y=0)

        ph = ImageTk.PhotoImage(self.image[2])
        self.fram = Frame(self.frame, height=100, width=200, bg='#2b2929', cursor='hand2')
        l1 = Label(self.fram, image=ph)
        l1.bind('<Button-1>', lambda a: self.get(key=2))
        l1.pack(side=LEFT, padx=10)
        self.fram.pack(side=LEFT)
        l1.image = ph
        self.fra = Frame(self.frame_label, height=60, width=200, bg='#2b2929')
        self.fra.pack(side=LEFT, padx=10)
        x = Label(self.fra, text=f'{self.title[2][:30]}...', width=30, fg='yellow', bg='#2b2929')
        x.place(x=0, y=0)
        #
        ph = ImageTk.PhotoImage(self.image[3])
        self.fram = Frame(self.frame, height=100, width=200, bg='#2b2929', cursor='hand2')
        l1 = Label(self.fram, image=ph)
        l1.bind('<Button-1>', lambda a: self.get(key=3))
        l1.pack(side=LEFT, padx=10)
        self.fram.pack(side=LEFT)
        l1.image = ph
        self.fra = Frame(self.frame_label, height=60, width=200, bg='#2b2929')
        self.fra.pack(side=LEFT, padx=10)
        x = Label(self.fra, text=f'{self.title[3][:30]}...', width=30, fg='yellow', bg='#2b2929')
        x.place(x=0, y=0)
        #
        ph = ImageTk.PhotoImage(self.image[4])
        self.fram = Frame(self.frame, height=100, width=200, bg='#2b2929', cursor='hand2')
        l1 = Label(self.fram, image=ph)
        l1.bind('<Button-1>', lambda a: self.get(key=4))
        l1.pack(side=LEFT, padx=10)
        self.fram.pack(side=LEFT)
        l1.image = ph
        self.fra = Frame(self.frame_label, height=60, width=200, bg='#2b2929')
        self.fra.pack(side=LEFT, padx=10)
        x = Label(self.fra, text=f'{self.title[4][:30]}...', width=30, fg='yellow', bg='#2b2929')
        x.place(x=0, y=0)
        #
        ph = ImageTk.PhotoImage(self.image[5])
        self.fram = Frame(self.frame, height=100, width=200, bg='#2b2929', cursor='hand2')
        l1 = Label(self.fram, image=ph)
        l1.bind('<Button-1>', lambda a: self.get(key=5))
        l1.pack(side=LEFT, padx=10)
        self.fram.pack(side=LEFT)
        l1.image = ph
        self.fra = Frame(self.frame_label, height=60, width=200, bg='#2b2929')
        self.fra.pack(side=LEFT, padx=10)
        x = Label(self.fra, text=f'{self.title[5][:30]}...', width=30, fg='yellow', bg='#2b2929')
        x.place(x=0, y=0)
        #
        ph = ImageTk.PhotoImage(self.image[6])
        self.fram = Frame(self.frame, height=100, width=200, bg='#2b2929', cursor='hand2')
        l1 = Label(self.fram, image=ph)
        l1.bind('<Button-1>', lambda a: self.get(key=6))
        l1.pack(side=LEFT, padx=10)
        self.fram.pack(side=LEFT)
        l1.image = ph
        self.fra = Frame(self.frame_label, height=60, width=200, bg='#2b2929')
        self.fra.pack(side=LEFT, padx=10)
        x = Label(self.fra, text=f'{self.title[6][:30]}...', width=30, fg='yellow', bg='#2b2929')
        x.place(x=0, y=0)
        #
        ph = ImageTk.PhotoImage(self.image[7])
        self.fram = Frame(self.frame, height=100, width=200, bg='#2b2929', cursor='hand2')
        l1 = Label(self.fram, image=ph)
        l1.bind('<Button-1>', lambda a: self.get(key=7))
        l1.pack(side=LEFT, padx=10)
        self.fram.pack(side=LEFT)
        l1.image = ph
        self.fra = Frame(self.frame_label, height=60, width=200, bg='#2b2929')
        self.fra.pack(side=LEFT, padx=10)
        x = Label(self.fra, text=f'{self.title[7][:30]}...', width=30, fg='yellow', bg='#2b2929')
        x.place(x=0, y=0)
        #
        ph = ImageTk.PhotoImage(self.image[8])
        self.fram = Frame(self.frame, height=100, width=200, bg='#2b2929', cursor='hand2')
        l1 = Label(self.fram, image=ph)
        l1.bind('<Button-1>', lambda a: self.get(key=8))
        l1.pack(side=LEFT, padx=10)
        self.fram.pack(side=LEFT)
        l1.image = ph
        self.fra = Frame(self.frame_label, height=60, width=200, bg='#2b2929')
        self.fra.pack(side=LEFT, padx=10)
        x = Label(self.fra, text=f'{self.title[8][:30]}...', width=30, fg='yellow', bg='#2b2929')
        x.place(x=0, y=0)
        #
        ph = ImageTk.PhotoImage(self.image[9])
        self.fram = Frame(self.frame, height=100, width=200, bg='#2b2929', cursor='hand2')
        l1 = Label(self.fram, image=ph)
        l1.bind('<Button-1>', lambda a: self.get(key=9))
        l1.pack(side=LEFT, padx=10)
        self.fram.pack(side=LEFT)
        l1.image = ph
        self.fra = Frame(self.frame_label, height=60, width=200, bg='#2b2929')
        self.fra.pack(side=LEFT, padx=10)
        x = Label(self.fra, text=f'{self.title[9][:30]}...', width=30, fg='yellow', bg='#2b2929')
        x.place(x=0, y=0)

        ph = ImageTk.PhotoImage(self.image[10])
        self.fram = Frame(self.frame, height=100, width=200, bg='#2b2929', cursor='hand2')
        l1 = Label(self.fram, image=ph)
        l1.bind('<Button-1>', lambda a: self.get(key=10))
        l1.pack(side=LEFT, padx=10)
        self.fram.pack(side=LEFT)
        l1.image = ph
        self.fra = Frame(self.frame_label, height=60, width=200, bg='#2b2929')
        self.fra.pack(side=LEFT, padx=10)
        x = Label(self.fra, text=f'{self.title[10][:30]}...', width=30, fg='yellow', bg='#2b2929')
        x.place(x=0, y=0)

        ph = ImageTk.PhotoImage(self.image[11])
        self.fram = Frame(self.frame, height=100, width=200, bg='#2b2929', cursor='hand2')
        l1 = Label(self.fram, image=ph)
        l1.bind('<Button-1>', lambda a: self.get(key=11))
        l1.pack(side=LEFT, padx=10)
        self.fram.pack(side=LEFT)
        l1.image = ph
        self.fra = Frame(self.frame_label, height=60, width=200, bg='#2b2929')
        self.fra.pack(side=LEFT, padx=10)
        x = Label(self.fra, text=f'{self.title[11][:30]}...', width=30, fg='yellow', bg='#2b2929')
        x.place(x=0, y=0)
        #

        ph = ImageTk.PhotoImage(self.image[12])
        self.fram = Frame(self.frame, height=100, width=200, bg='#2b2929', cursor='hand2')
        l1 = Label(self.fram, image=ph)
        l1.bind('<Button-1>', lambda a: self.get(key=12))
        l1.pack(side=LEFT, padx=10)
        self.fram.pack(side=LEFT)
        l1.image = ph
        self.fra = Frame(self.frame_label, height=60, width=200, bg='#2b2929')
        self.fra.pack(side=LEFT, padx=10)
        x = Label(self.fra, text=f'{self.title[12][:30]}...', width=30, fg='yellow', bg='#2b2929')
        x.place(x=0, y=0)

        ph = ImageTk.PhotoImage(self.image[13])
        self.fram = Frame(self.frame, height=100, width=200, bg='#2b2929', cursor='hand2')
        l1 = Label(self.fram, image=ph)
        l1.bind('<Button-1>', lambda a: self.get(key=13))
        l1.pack(side=LEFT, padx=10)
        self.fram.pack(side=LEFT)
        l1.image = ph
        self.fra = Frame(self.frame_label, height=60, width=200, bg='#2b2929')
        self.fra.pack(side=LEFT, padx=10)
        x = Label(self.fra, text=f'{self.title[13][:30]}...', width=30, fg='yellow', bg='#2b2929')
        x.place(x=0, y=0)

        ph = ImageTk.PhotoImage(self.image[14])
        self.fram = Frame(self.frame, height=100, width=200, bg='#2b2929', cursor='hand2')
        l1 = Label(self.fram, image=ph)
        l1.bind('<Button-1>', lambda a: self.get(key=14))
        l1.pack(side=LEFT, padx=10)
        self.fram.pack(side=LEFT)
        l1.image = ph
        self.fra = Frame(self.frame_label, height=60, width=200, bg='#2b2929')
        self.fra.pack(side=LEFT, padx=10)
        x = Label(self.fra, text=f'{self.title[14][:30]}...', width=30, fg='yellow', bg='#2b2929')
        x.place(x=0, y=0)

        ph = ImageTk.PhotoImage(self.image[15])
        self.fram = Frame(self.frame, height=100, width=200, bg='#2b2929', cursor='hand2')
        l1 = Label(self.fram, image=ph)
        l1.bind('<Button-1>', lambda a: self.get(key=15))
        l1.pack(side=LEFT, padx=10)
        self.fram.pack(side=LEFT)
        l1.image = ph
        self.fra = Frame(self.frame_label, height=60, width=200, bg='#2b2929')
        self.fra.pack(side=LEFT, padx=10)
        x = Label(self.fra, text=f'{self.title[15][:30]}...', width=30, fg='yellow', bg='#2b2929')
        x.place(x=0, y=0)

        ph = ImageTk.PhotoImage(self.image[16])
        self.fram = Frame(self.frame, height=100, width=200, bg='#2b2929', cursor='hand2')
        l1 = Label(self.fram, image=ph)
        l1.bind('<Button-1>', lambda a: self.get(key=16))
        l1.pack(side=LEFT, padx=10)
        self.fram.pack(side=LEFT)
        l1.image = ph
        self.fra = Frame(self.frame_label, height=60, width=200, bg='#2b2929')
        self.fra.pack(side=LEFT, padx=10)
        x = Label(self.fra, text=f'{self.title[16][:30]}...', width=30, fg='yellow', bg='#2b2929')
        x.place(x=0, y=0)

        self.canvas.create_window(0, 0, anchor='n', window=self.frame, height=180)
        self.canvas.update_idletasks()
        self.canvas.create_window(0, 180, anchor='n', window=self.frame_label, height=160)
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox('all'),xscrollcommand=self.scroll_y.set, bg='#2b2929')
        self.canvas.pack()
        self.scroll_y.pack(fill='x')

        self.f = Frame(self.master, height=100, width=1536, bg='#2b2929')
        self.f.pack()
        self.bottom_strip = Frame(self.master, height=5, width=1536, bg='red')
        self.bottom_strip.pack()
        self.footer = Frame(self.master, height=50, width=1536, bg='#5e615e')
        self.footer.pack()


    def entry_box(self,cx=410,cy = 30,bx= 630,by = 85):
        self.lst = self.d['title'].values
        self.entrt = Frame(self.bottom, height=100, bg='grey')
        self.entrt.place(x=1300, y=500)
        self.entry = AutocompleteEntry(self.entrt)
        self.entry.set_completion_list(self.lst)
        self.entry.place(x=700, y=500)
        self.entry.focus_set()
        self.combo = AutocompleteCombobox(self.bottom, width=25, height=15, font="Verdana 25")
        self.combo.set_completion_list(self.lst)
        bigfont = Font(family="Helvetica", size=20)
        self.combo.option_add("*TCombobox*Listbox*Font", bigfont)
        self.combo.place(x=cx, y=cy)
        self.combo.focus_set()
        self.search_button = Button(self.bottom, text='Search', font="Verdana 13", command=self.search)
        self.search_button.bind('<Return>', self.search)
        self.search_button.place(x=bx, y=by)

    def get(self, key):
        self.key = key
        self.search()
        self.key = -1

    def search(self, _event=None):
        if self.no>0:
            self.canvas.destroy()
            self.f.destroy()
            self.bottom_strip.destroy()
            self.footer.destroy()
            self.scroll_y.destroy()
        self.no+=1
        if self.key!=-1:
            title = self.title[self.key]
        else:
            title = self.combo.get()
        doc_id = self.d[self.d['title']==title].index[0]
        # print(self.d[self.d['title']==title]['asin'].values[0])
        self.img = Image.open(f"16k_images/{self.d[self.d['title']==title]['asin'].values[0]}.jpeg")
        newimage = self.img.resize((150, 200))
        self.ph1 = ImageTk.PhotoImage(newimage)
        self.Original_Image = Label(self.bottom,image = self.ph1)
        self.Original_Image.place(x = 1030,y = 10)
        myfont = Font(family='Ink Free', size=15, weight='bold')
        f = Label(self.bottom, text=f"ASIN  ", bg="#2b2929", fg='#6dad86',font=myfont)
        f.place(x=1200, y=20)
        g = Label(self.bottom,text = f": {self.d[self.d['title']==title]['asin'].values[0]}",bg = "#2b2929",justify = LEFT,fg='#d3dbdb',font = myfont)
        g.place(x = 1260,y = 20)

        f = Label(self.bottom, text=f" {title[:40].strip()}\n  {title[40:]}  ", bg="#2b2929",justify=CENTER, fg='#02f733', font=myfont)
        f.place(x=920, y=220)

        f = Label(self.bottom, text=f"Brand  ", bg="#2b2929", fg='#6dad86', font=myfont)
        f.place(x=1200, y=65)
        f = Label(self.bottom, text=f": {self.d[self.d['title'] == title]['brand'].values[0]}  ", bg="#2b2929", fg='white', font=myfont)
        f.place(x=1260, y=65)

        f = Label(self.bottom, text=f"Color  ", bg="#2b2929", fg='#6dad86', font=myfont)
        f.place(x=1200, y=110)
        f = Label(self.bottom, text=f": {self.d[self.d['title'] == title]['color'].values[0]}  ", bg="#2b2929",fg='white', font=myfont)
        f.place(x=1260, y=110)

        f = Label(self.bottom, text=f"Price  ", bg="#2b2929", fg='#6dad86', font=myfont)
        f.place(x=1200, y=155)
        f = Label(self.bottom, text=f": {self.d[self.d['title'] == title]['formatted_price'].values[0]}  ", bg="#2b2929",fg='white', font=myfont)
        f.place(x=1260, y=155)
        self.Ml_model(doc_id)
        self.update_list()

def main():
    root = Tk(className=' AutocompleteEntry demo')
    app = Application(root)
    root.title("Product Recommendation")
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    print(root.winfo_screenwidth())
    root.resizable(False, False)

    root.mainloop()


if __name__ == '__main__':
    main()