# tkinterのインポート
import tkinter as tk
import tkinter.ttk as ttk
import readcard


def change_app():
    frame2.tkraise()

def change_main():
    frame.tkraise()

def ReadCard(event):
    message = readcard.ReadCard_Post(teacher_id)
    label.config(text=message)

def getTextInput():
    global teacher_id
    teacher_id = entry1_frame.get()
    #print(teacher_id)

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
    frame = tk.Frame(root, bg='RoyalBlue2')
    frame.grid(row=0, column=0, sticky="nsew", pady=20)

    # 各種ウィジェットの作成
    label1_frame = ttk.Label(frame, text='教員IDを入力してください', foreground='White', font=(
        "20"), background='RoyalBlue2')
    label2_frame = ttk.Label(
        frame, text='教員ID', foreground='White', background='RoyalBlue2')
    entry1_frame = ttk.Entry(frame, width=30)

    #label3_frame = ttk.Label(frame,text='講義ID',foreground='White',background='RoyalBlue2')
    #entry2_frame = ttk.Entry(frame,width=30)
    teacher_id:str
    button_change = ttk.Button(frame, text="OK", command=lambda:[change_app(),getTextInput()])
    # クリックしたらデータ取得
    # 各種ウィジェットの設置(ピクセル単位で指定)
    label1_frame.place(x=250, y=0)
    label2_frame.place(x=365, y=40)
    entry1_frame.place(x=300, y=70)
    # label3_frame.place(x=365,y=100)
    # entry2_frame.place(x=300,y=130)
    button_change.place(x=350, y=250)

    # フレーム作成
    frame2 = ttk.Frame(root)
    frame2.grid(row=0, column=0, sticky="nsew", pady=20)

    # 各種ウィジェットの作成
    label1_frame2 = ttk.Label(
        frame2, text='カードを読み込むには実行ボタンを押してください', foreground='RoyalBlue3', font=("20"))
    button_start = ttk.Button(frame2, text="実行")

    # Label (新規追加)
    label = ttk.Label(frame2, font="20", justify="center")
    label.pack()

    # 結果表示
    button_start.bind("<Button-1>", ReadCard)

    button_change = ttk.Button(frame2, text="戻る", command=change_main)

    # 各種ウィジェットの設置
    label1_frame2.place(x=160, y=100)
    button_start.place(x=350, y=200)
    button_change.place(x=350, y=320)

    # frameを前面にする
    frame.tkraise()

    root.mainloop()
