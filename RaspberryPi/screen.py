import tkinter as tk
import tkinter.ttk as ttk

def btn_click1():

    baseGround.destroy()

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
    #GUIの画面タイトル
    if T_ID == 'P001' and L_ID == 'T4':
        baseGround_new_csv4.title('応用数学')
    elif T_ID == 'P001' and L_ID == 'T5':
        baseGround_new_csv4.title('数学演習')
    elif T_ID == 'P002' and L_ID == 'W5_1':
        baseGround_new_csv4.title('保健体育')
    elif T_ID == 'P003' and L_ID == 'M1':
        baseGround_new_csv4.title('心理学')
    elif T_ID == 'P004' and L_ID == 'W12':
        baseGround_new_csv4.title('プログラミング')
    elif T_ID == 'P005' and L_ID == 'Th5_1':
        baseGround_new_csv4.title('電磁気学')
    elif T_ID == 'P006' and L_ID == 'F2':
        baseGround_new_csv4.title('情報ネットワーク')
    elif T_ID == 'P007' and L_ID == 'M4':
        baseGround_new_csv4.title('システム開発演習')
    elif T_ID == 'P007' and L_ID == 'Th34':
        baseGround_new_csv4.title('情報工学実習')
    elif T_ID == 'P008' and L_ID == 'M3':
        baseGround_new_csv4.title('情報理論')
    elif T_ID == 'P008' and L_ID == 'F3':
        baseGround_new_csv4.title('アルゴリズムとデータ構造')
    elif T_ID == 'P009' and L_ID == 'W3_1':
        baseGround_new_csv4.title('経済学')
    elif T_ID == 'P010' and L_ID == 'T2':
        baseGround_new_csv4.title('英会話')
    elif T_ID == 'P011' and L_ID == 'M2':
        baseGround_new_csv4.title('教養英語')
    elif T_ID == 'P011' and L_ID == 'F1':
        baseGround_new_csv4.title('科学英語')
    elif T_ID == 'P012' and L_ID == 'T3_2':
        baseGround_new_csv4.title('物理学')
    elif T_ID == 'P013' and L_ID == 'W5_2':
        baseGround_new_csv4.title('コミュニケーション入門')
    elif T_ID == 'P014' and L_ID == 'Th5_2':
        baseGround_new_csv4.title('電子回路学')
    elif T_ID == 'P015' and L_ID == 'W4':
        baseGround_new_csv4.title('信号処理')
    elif T_ID == 'P016' and L_ID == 'W3_2':
        baseGround_new_csv4.title('文学・文化学')

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



#メインウィンドウ
baseGround = tk.Tk()
# GUIの画面サイズ
baseGround.geometry('800x480')
#GUIの画面タイトル
baseGround.title('初期画面')


#ラベルとテキストボックス
label = tk.Label(text = '教員IDと講義IDを入力してください',foreground='white', background='black',font=("20"))
label.pack(padx = 10, pady = 30)
label = tk.Label(text = '教員IDを入力してください')
label.pack(padx = 10, pady = 0)
text1 = tk.Entry(width=30)
text1.pack(padx = 10, pady = 0)
label = tk.Label(text = '講義IDを入力してください')
label.pack(padx = 10, pady = 0)
text2 = tk.Entry(width=30)
text2.pack(padx = 10, pady = 0)
#ボタン
btn = tk.Button(baseGround, text='OK', command=btn_click).pack(padx = 10, pady = 100)
#表示
baseGround.mainloop()