## tkinterのインポート
import tkinter as tk
import tkinter.ttk as ttk

def change_app():
    frame2.tkraise()

def change_main():
    frame.tkraise()



if __name__ == "__main__":
    # rootメインウィンドウの設定
    root = tk.Tk()
    root.title("")
    root.geometry("800x400")

    # rootメインウィンドウのグリッドを 1x1 にする
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.configure(bg='yellow2')


    # メインフレームの作成と設置
    frame = tk.Frame(root,bg='RoyalBlue2')
    frame.grid(row=0, column=0, sticky="nsew", pady=20)

    # 各種ウィジェットの作成
    label1_frame = ttk.Label(frame, text = '教員IDと講義IDを入力してください',foreground='White',font=("20"),background='RoyalBlue2')
    label2_frame = ttk.Label(frame, text='教員ID',foreground='White',background='RoyalBlue2')
    entry1_frame = ttk.Entry(frame,width=30)
    label3_frame = ttk.Label(frame,text='講義ID',foreground='White',background='RoyalBlue2')
    entry2_frame = ttk.Entry(frame,width=30)
    button_change = ttk.Button(frame, text="OK", command=change_app)

    # 各種ウィジェットの設置(ピクセル単位で指定)
    label1_frame.place(x=240,y=0)
    label2_frame.place(x=365,y=40)
    entry1_frame.place(x=300,y=70)
    label3_frame.place(x=365,y=100)
    entry2_frame.place(x=300,y=130)
    button_change.place(x=350,y=250)





    #フレーム作成
    frame2 = ttk.Frame(root)
    frame2.grid(row=0, column=0, sticky="nsew", pady=20)

    # 各種ウィジェットの作成
    label1_frame2 = ttk.Label(frame2, text = 'カードをタップしてください',foreground='RoyalBlue3',font=("20"))
    button_change = ttk.Button(frame2, text="戻る", command=change_main)

    # 各種ウィジェットの設置
    label1_frame2.pack()
    button_change.pack()

    # frameを前面にする
    frame.tkraise()


    

    root.mainloop()