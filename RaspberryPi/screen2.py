## tkinterのインポート
import tkinter as tk
import tkinter.ttk as ttk

def change_app():
    frame2.tkraise()

def change_main():
    frame.tkraise()

def btn_click1():
    frame_card = ttk.Frame(root)

    # GUIの画面サイズ
    frame_card.geometry('800x480')
    #GUIの画面タイトル
    frame_card.title('結果画面1')
    #ラベル
    label = tk.Label(frame_card, text = '時間内での出席を確認しました',foreground='white', background='black').pack(padx = 20, pady = 40)
    # ボタン
    btn_return = tk.Button(frame_card, text='待機画面に戻る', command=frame2).pack(padx = 20, pady = 30)
    root.mainloop()




if __name__ == "__main__":
    # rootメインウィンドウの設定
    root = tk.Tk()
    root.title("")
    root.geometry("800x400")

    # rootメインウィンドウのグリッドを 1x1 にする
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)


    # メインフレームの作成と設置
    frame = ttk.Frame(root)
    frame.grid(row=0, column=0, sticky="nsew", pady=20)

    # 各種ウィジェットの作成
    label1_frame = ttk.Label(frame, text = '教員IDと講義IDを入力してください',foreground='white', background='black',font=("20"))
    label2_frame = ttk.Label(frame, text='教員IDを入力してください')
    entry1_frame = ttk.Entry(frame,width=30)
    label3_frame = ttk.Label(frame,text='講義IDを入力してください')
    entry2_frame = ttk.Entry(frame,width=30)
    button_change = ttk.Button(frame, text="OK", command=change_app)

    # 各種ウィジェットの設置
    label1_frame.pack()
    label2_frame.pack()
    entry1_frame.pack()
    label3_frame.pack()
    entry2_frame.pack()
    button_change.pack()

    #フレーム作成
    frame2 = ttk.Frame(root)
    frame2.grid(row=0, column=0, sticky="nsew", pady=20)

    # 生徒のログイン画面作成
    label1_frame_app = ttk.Label(frame2, text="カードをタップしてください")
    ttk.Button(frame2,text='時間内に出席',command=btn_click1)

    button_change_frame_app = ttk.Button(frame2, text="メインウィンドウに移動", command=change_main)

    # 各種ウィジェットの設置
    label1_frame_app.pack()
    button_change_frame_app.pack()

    # frameを前面にする
    frame.tkraise()


    root.mainloop()