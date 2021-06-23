import tkinter as tk

def btn_click1():

    #最初のGUIの画面に戻る
    def return_view():
        baseGround_new_csv1.destroy()

    baseGround_new_csv1 = tk.Tk()
    # GUIの画面サイズ
    baseGround_new_csv1.geometry('800x480')
    #GUIの画面タイトル
    baseGround_new_csv1.title('結果画面1')
    #ラベル
    label = tk.Label(baseGround_new_csv1, text = '時間内での出席を確認しました',foreground='white', background='black').pack(padx = 20, pady = 40)
    # ボタン
    btn_return = tk.Button(baseGround_new_csv1, text='待機画面に戻る', command=return_view).pack(padx = 20, pady = 30)
    baseGround_new_csv1.mainloop()

def btn_click2():

    #最初のGUIの画面に戻る
    def return_view():
        baseGround_new_csv2.destroy()

    baseGround_new_csv2 = tk.Tk()
    # GUIの画面サイズ
    baseGround_new_csv2.geometry('800x480')
    #GUIの画面タイトル
    baseGround_new_csv2.title('結果画面2')
    #ラベル
    label = tk.Label(baseGround_new_csv2, text = '遅刻での出席を確認しました',foreground='white', background='black').pack(padx = 20, pady = 40)
    # ボタン
    btn_return = tk.Button(baseGround_new_csv2, text='待機画面に戻る', command=return_view)
    btn_return.pack()
    baseGround_new_csv2.mainloop()

def btn_click3():

    #最初のGUIの画面に戻る
    def return_view():
        baseGround_new_csv3.destroy()

    baseGround_new_csv3 = tk.Tk()
    # GUIの画面サイズ
    baseGround_new_csv3.geometry('800x480')
    #GUIの画面タイトル
    baseGround_new_csv3.title('結果画面3')
    #ラベル
    label = tk.Label(baseGround_new_csv3, text = 'この教科の名簿に登録されていません', foreground='white', background='red').pack(padx = 0, pady = 30)
    label = tk.Label(baseGround_new_csv3, text = 'もう一度部屋を確認してください', foreground='white', background='red').pack(padx = 0, pady = 0)
    # ボタン
    btn_return = tk.Button(baseGround_new_csv3, text='待機画面に戻る', command=return_view).pack(padx = 10, pady = 10)
    baseGround_new_csv3.mainloop()

def btn_click():
    #最初のGUIの画面に戻る
    def return_view():
        baseGround_new_csv4.destroy()
    
    baseGround_new_csv4 = tk.Tk()

    T_ID = text1.get() #先生のID
    L_ID = text2.get() #講義のID

    # GUIの画面サイズ
    baseGround_new_csv4.geometry('800x480')

    #ラベル
    label = tk.Label(baseGround_new_csv4,text = 'カードをタップしてください', foreground='white', background='black')
    label.pack()
    # ボタン
    btn1 = tk.Button(baseGround_new_csv4, text='時間内に出席', command=btn_click1)
    btn1.pack()

    btn2 = tk.Button(baseGround_new_csv4, text='遅刻', command=btn_click2)
    btn2.pack()

    btn3 = tk.Button(baseGround_new_csv4, text='教科間違い', command=btn_click3)
    btn3.pack()

    btn_return = tk.Button(baseGround_new_csv4, text='初期画面に戻る', command=return_view).pack(padx = 30, pady = 40)
 
    #表示
    baseGround_new_csv4.mainloop()


baseGround = tk.Tk()
# GUIの画面サイズ
baseGround.geometry('800x480')
#GUIの画面タイトル
baseGround.title('初期画面')

#ラベルとテキストボックス
label = tk.Label(text = '教員IDと講義IDを入力してください',foreground='white', background='black')
label.pack()
label = tk.Label(text = '教員IDを入力してください')
label.pack()
text1 = tk.Entry(width=30)
text1.pack()
label = tk.Label(text = '講義IDを入力してください')
label.pack()
text2 = tk.Entry(width=30)
text2.pack()
#ボタン
btn = tk.Button(baseGround, text='OK', command=btn_click).pack(padx = 10, pady = 40)
#表示
baseGround.mainloop()