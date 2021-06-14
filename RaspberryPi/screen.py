import tkinter as tk
 
def btn_click1():

    #最初のGUIの画面に戻る
    def return_view():
        baseGround_new_csv1.destroy()

    baseGround_new_csv1 = tk.Tk()
    # GUIの画面サイズ
    baseGround_new_csv1.geometry('300x200')
    #GUIの画面タイトル
    baseGround_new_csv1.title('結果画面1')
    #ラベル
    label = tk.Label(baseGround_new_csv1, text = '時間内での出席を確認しました', foreground='white', background='black')
    label.pack()
    # ボタン
    btn_return = tk.Button(baseGround_new_csv1, text='待機画面に戻る', command=return_view)
    btn_return.pack()
    baseGround_new_csv1.mainloop()

def btn_click2():

    #最初のGUIの画面に戻る
    def return_view():
        baseGround_new_csv2.destroy()

    baseGround_new_csv2 = tk.Tk()
    # GUIの画面サイズ
    baseGround_new_csv2.geometry('300x200')
    #GUIの画面タイトル
    baseGround_new_csv2.title('結果画面2')
    #ラベル
    label = tk.Label(baseGround_new_csv2, text = '遅刻での出席を確認しました', foreground='white', background='black')
    label.pack()
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
    baseGround_new_csv3.geometry('300x200')
    #GUIの画面タイトル
    baseGround_new_csv3.title('結果画面3')
    #ラベル
    label = tk.Label(baseGround_new_csv3, text = 'この教科の名簿に登録されていません', foreground='white', background='red')
    label.pack()
    label = tk.Label(baseGround_new_csv3, text = 'もう一度部屋を確認してください', foreground='white', background='red')
    label.pack()
    # ボタン
    btn_return = tk.Button(baseGround_new_csv3, text='待機画面に戻る', command=return_view)
    btn_return.pack()
    baseGround_new_csv3.mainloop()

baseGround = tk.Tk()
# GUIの画面サイズ
baseGround.geometry('300x200')
#GUIの画面タイトル
baseGround.title('待機画面')

#ラベル
label = tk.Label(text = 'カードをタップしてください', foreground='white', background='black')
label.pack()

# ボタン
btn1 = tk.Button(baseGround, text='時間内に出席', command=btn_click1)
btn1.pack()

btn2 = tk.Button(baseGround, text='遅刻', command=btn_click2)
btn2.pack()

btn3 = tk.Button(baseGround, text='教科間違い', command=btn_click3)
btn3.pack()
 
#表示
baseGround.mainloop()