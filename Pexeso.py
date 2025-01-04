from tkinter import*
from tkinter import messagebox
from PIL import ImageTk, Image


root = Tk()
root.title("pexseso")
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (width,height))


pocet_otoc = 0
prva = ""
i = 0
kliknute_pole = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ratanie = 0

def otacanie0(event):
    global prva,i,kliknute_pole,pocet_otoc,ratanie
    if (pocet_otoc<=2): 
        pocet_otoc = pocet_otoc + 1
        otaznik_label0.config(image=HZfotka_ac_source)
        kliknute_pole[0] = 1

    if pocet_otoc==1:
        prva = 'otaznik_label0'
        i = 0
        

    if (pocet_otoc==2): 
      
        if (kliknute_pole[0] == 1) and ( kliknute_pole[6] ==1):
            otaznik_label0.config(image=HZfotka_ac_source)
            otaznik_label06.config(image=HZfotka_ac_source_text)  
        
                      
        else:   
            otaznik_label0.after(ms=1000,func=lambda:otaznik_label0.config(image=HZfotka_otaznik0))
            eval(f"{prva}.after(ms=1000,func=lambda:{prva}.config(image=HZfotka_otaznik0))")
            kliknute_pole[0] = 0
            kliknute_pole[i] = 0 
            prva = ""
            i = 0
        pocet_otoc = 0
        ratanie +=1

def otacanie1(event):
    global prva,i,kliknute_pole,pocet_otoc,ratanie
    if (pocet_otoc<=2): 
        pocet_otoc = pocet_otoc + 1
        otaznik_label01.config(image=HZfotka_kondenzator)
        kliknute_pole[1] = 1

    if pocet_otoc==1:
        prva = 'otaznik_label01'
        i = 1

    if (pocet_otoc==2): 
      
        if (kliknute_pole[1] == 1) and ( kliknute_pole[2] ==1):
            otaznik_label01.config(image=HZfotka_kondenzator)
            otaznik_label02.config(image=HZfotka_kondenzator_text) 
            
                        
        else:   
            otaznik_label01.after(ms=1000,func=lambda:otaznik_label01.config(image=HZfotka_otaznik0))
            eval(f"{prva}.after(ms=1000,func=lambda:{prva}.config(image=HZfotka_otaznik0))")
            kliknute_pole[1] = 0
            kliknute_pole[i] = 0 
            prva = ""
            i = 0
        pocet_otoc = 0
        ratanie +=1

    
def otacanie2(event):
    global prva,i,kliknute_pole,pocet_otoc,ratanie
    if (pocet_otoc<=2): 
        pocet_otoc = pocet_otoc + 1
        otaznik_label02.config(image=HZfotka_kondenzator_text)
        kliknute_pole[2] = 1

    if pocet_otoc==1:
        prva = 'otaznik_label02'
        i = 2

    if (pocet_otoc==2): 
      
        if (kliknute_pole[2] == 1) and ( kliknute_pole[1] ==1):
            otaznik_label02.config(image=HZfotka_kondenzator_text)   
            otaznik_label01.config(image=HZfotka_kondenzator)
                        
        else:   
            otaznik_label02.after(ms=1000,func=lambda:otaznik_label02.config(image=HZfotka_otaznik0))
            eval(f"{prva}.after(ms=1000,func=lambda:{prva}.config(image=HZfotka_otaznik0))")
            kliknute_pole[2] = 0
            kliknute_pole[i] = 0 
            prva = ""
            i = 0
        pocet_otoc = 0
        ratanie +=1


def otacanie3(event):
    global prva,i,kliknute_pole,pocet_otoc,ratanie
    if (pocet_otoc<=2): 
        pocet_otoc = pocet_otoc + 1
        otaznik_label03.config(image=HZfotka_dioda_text)
        kliknute_pole[3] = 1

    if pocet_otoc==1:
        prva = 'otaznik_label03'
        i = 3

    if (pocet_otoc==2): 
      
        if (kliknute_pole[3] == 1) and ( kliknute_pole[8] ==1):
            otaznik_label03.after(ms=1000,func=lambda:otaznik_label03.config(image=HZfotka_dioda_text))   
            otaznik_label08.after(ms=1000,func=lambda:otaznik_label08.config(image=HZfotka_dioda))
                        
        else:   
            otaznik_label03.after(ms=1000,func=lambda:otaznik_label03.config(image=HZfotka_otaznik0))
            eval(f"{prva}.after(ms=1000,func=lambda:{prva}.config(image=HZfotka_otaznik0))")
            kliknute_pole[3] = 0
            kliknute_pole[i] = 0 
            prva = ""
            i = 0
        pocet_otoc = 0
        ratanie +=1
    


def otacanie4(event):
    global prva,i,kliknute_pole,pocet_otoc,ratanie
    if (pocet_otoc<=2): 
        pocet_otoc = pocet_otoc + 1
        otaznik_label04.config(image=HZfotka_cievka_text)
        kliknute_pole[4] = 1

    if pocet_otoc==1:
        prva = 'otaznik_label04'
        i = 4

    if (pocet_otoc==2): 
      
        if (kliknute_pole[4] == 1) and ( kliknute_pole[10] ==1):
            otaznik_label04.after(ms=1000,func=lambda:otaznik_label04.config(image=HZfotka_cievka_text))   
            otaznik_label10.after(ms=1000,func=lambda:otaznik_label10.config(image=HZfotka_cievka))
                        
        else:   
            otaznik_label04.after(ms=1000,func=lambda:otaznik_label04.config(image=HZfotka_otaznik0))
            eval(f"{prva}.after(ms=1000,func=lambda:{prva}.config(image=HZfotka_otaznik0))")
            kliknute_pole[4] = 0
            kliknute_pole[i] = 0 
            prva = ""
            i = 0
        pocet_otoc = 0
        ratanie +=1
       


def otacanie5(event):
    global prva,i,kliknute_pole,pocet_otoc,ratanie
    if (pocet_otoc<=2): 
        pocet_otoc = pocet_otoc + 1
        otaznik_label05.config(image=HZfotka_rezistor)
        kliknute_pole[5] = 1

    if pocet_otoc==1:
        prva = 'otaznik_label05'
        i = 5

    if (pocet_otoc==2): 
      
        if (kliknute_pole[5] == 1) and ( kliknute_pole[14] ==1):
            otaznik_label05.after(ms=1000,func=lambda:otaznik_label05.config(image=HZfotka_rezistor))   
            otaznik_label14.after(ms=1000,func=lambda:otaznik_label14.config(image=HZfotka_rezistor_text))
                        
        else:   
            otaznik_label05.after(ms=1000,func=lambda:otaznik_label05.config(image=HZfotka_otaznik0))
            eval(f"{prva}.after(ms=1000,func=lambda:{prva}.config(image=HZfotka_otaznik0))")
            kliknute_pole[5] = 0
            kliknute_pole[i] = 0 
            prva = ""
            i = 0
        pocet_otoc = 0
        ratanie +=1

def otacanie6(event):
    global prva,i,kliknute_pole,pocet_otoc,ratanie
    if (pocet_otoc<=2): 
        pocet_otoc = pocet_otoc + 1
        otaznik_label06.config(image=HZfotka_ac_source_text)
        kliknute_pole[6] = 1

    if pocet_otoc==1:
        prva = 'otaznik_label06'
        i = 6

    if (pocet_otoc==2): 
      
        if (kliknute_pole[6] == 1) and ( kliknute_pole[0] ==1):
            otaznik_label06.config(image=HZfotka_ac_source_text) 
            otaznik_label0.config(image=HZfotka_ac_source)
                        
        else:   
            otaznik_label06.after(ms=1000,func=lambda:otaznik_label06.config(image=HZfotka_otaznik0))
            eval(f"{prva}.after(ms=1000,func=lambda:{prva}.config(image=HZfotka_otaznik0))")
            kliknute_pole[6] = 0
            kliknute_pole[i] = 0 
            prva = ""
            i = 0
        pocet_otoc = 0
        ratanie +=1
    

def otacanie7(event):
    global prva,i,kliknute_pole,pocet_otoc,ratanie
    if (pocet_otoc<=2): 
        pocet_otoc = pocet_otoc + 1
        otaznik_label07.config(image=HZfotka_transformator_text)
        kliknute_pole[7] = 1

    if pocet_otoc==1:
        prva = 'otaznik_label07'
        i = 7

    if (pocet_otoc==2): 
      
        if (kliknute_pole[7] == 1) and ( kliknute_pole[9] ==1):
            otaznik_label07.after(ms=1000,func=lambda:otaznik_label07.config(image=HZfotka_transformator_text))   
            otaznik_label09.after(ms=1000,func=lambda:otaznik_label09.config(image=HZfotka_transformator))
                        
        else:   
            otaznik_label07.after(ms=1000,func=lambda:otaznik_label07.config(image=HZfotka_otaznik0))
            eval(f"{prva}.after(ms=1000,func=lambda:{prva}.config(image=HZfotka_otaznik0))")
            kliknute_pole[7] = 0
            kliknute_pole[i] = 0 
            prva = ""
            i = 0
        pocet_otoc = 0
        ratanie +=1

def otacanie8(event):
    global prva,i,kliknute_pole,pocet_otoc,ratanie
    if (pocet_otoc<=2): 
        pocet_otoc = pocet_otoc + 1
        otaznik_label08.config(image=HZfotka_dioda)
        kliknute_pole[8] = 1

    if pocet_otoc==1:
        prva = 'otaznik_label08'
        i = 8

    if (pocet_otoc==2): 
      
        if (kliknute_pole[8] == 1) and ( kliknute_pole[3] ==1):
            otaznik_label08.after(ms=1000,func=lambda:otaznik_label08.config(image=HZfotka_dioda))
            otaznik_label03.after(ms=1000,func=lambda:otaznik_label03.config(image=HZfotka_dioda_text))   
            
            
        else:   
            otaznik_label08.after(ms=1000,func=lambda:otaznik_label08.config(image=HZfotka_otaznik0))
            eval(f"{prva}.after(ms=1000,func=lambda:{prva}.config(image=HZfotka_otaznik0))")
            kliknute_pole[8] = 0
            kliknute_pole[i] = 0 
            prva = ""
            i = 0
        pocet_otoc = 0
        ratanie +=1

def otacanie9(event):
    global prva,i,kliknute_pole,pocet_otoc,ratanie
    if (pocet_otoc<=2): 
        pocet_otoc = pocet_otoc + 1
        otaznik_label09.config(image=HZfotka_transformator)
        kliknute_pole[9] = 1

    if pocet_otoc==1:
        prva = 'otaznik_label09'
        i = 9

    if (pocet_otoc==2): 
      
        if (kliknute_pole[9] == 1) and ( kliknute_pole[7] ==1):
            otaznik_label09.after(ms=1000,func=lambda:otaznik_label09.config(image=HZfotka_transformator))
            otaznik_label07.after(ms=1000,func=lambda:otaznik_label07.config(image=HZfotka_transformator_text))   
            
            
        else:   
            otaznik_label09.after(ms=1000,func=lambda:otaznik_label09.config(image=HZfotka_otaznik0))
            eval(f"{prva}.after(ms=1000,func=lambda:{prva}.config(image=HZfotka_otaznik0))")
            kliknute_pole[9] = 0
            kliknute_pole[i] = 0 
            prva = ""
            i = 0
        pocet_otoc = 0
        ratanie +=1

def otacanie10(event):
    global prva,i,kliknute_pole,pocet_otoc,ratanie
    if (pocet_otoc<=2): 
        pocet_otoc = pocet_otoc + 1
        otaznik_label10.config(image=HZfotka_cievka)
        kliknute_pole[10] = 1

    if pocet_otoc==1:
        prva = 'otaznik_label10'
        i = 10

    if (pocet_otoc==2): 
      
        if (kliknute_pole[10] == 1) and ( kliknute_pole[4] ==1):
            otaznik_label10.after(ms=1000,func=lambda:otaznik_label10.config(image=HZfotka_cievka))
            otaznik_label04.after(ms=1000,func=lambda:otaznik_label04.config(image=HZfotka_cievka_text))   
            
            
        else:   
            otaznik_label10.after(ms=1000,func=lambda:otaznik_label10.config(image=HZfotka_otaznik0))
            eval(f"{prva}.after(ms=1000,func=lambda:{prva}.config(image=HZfotka_otaznik0))")
            kliknute_pole[10] = 0
            kliknute_pole[i] = 0 
            prva = ""
            i = 0
        pocet_otoc = 0
        ratanie +=1
        


def otacanie11(event):
    global prva,i,kliknute_pole,pocet_otoc,ratanie
    if (pocet_otoc<=2): 
        pocet_otoc = pocet_otoc + 1
        otaznik_label11.config(image=HZfotka_tranzistor_text)
        kliknute_pole[11] = 1

    if pocet_otoc==1:
        prva = 'otaznik_label11'
        i = 11

    if (pocet_otoc==2): 
      
        if (kliknute_pole[11] == 1) and ( kliknute_pole[12] ==1):
            otaznik_label11.after(ms=1000,func=lambda:otaznik_label11.config(image=HZfotka_tranzistor_text))
            otaznik_label12.after(ms=1000,func=lambda:otaznik_label12.config(image=HZfotka_tranzistor))   
            
            
        else:   
            otaznik_label11.after(ms=1000,func=lambda:otaznik_label11.config(image=HZfotka_otaznik0))
            eval(f"{prva}.after(ms=1000,func=lambda:{prva}.config(image=HZfotka_otaznik0))")
            kliknute_pole[11] = 0
            kliknute_pole[i] = 0 
            prva = ""
            i = 0
        pocet_otoc = 0
        ratanie +=1

def otacanie12(event):
    global prva,i,kliknute_pole,pocet_otoc,ratanie
    if (pocet_otoc<=2): 
        pocet_otoc = pocet_otoc + 1
        otaznik_label12.config(image=HZfotka_tranzistor)
        kliknute_pole[12] = 1

    if pocet_otoc==1:
        prva = 'otaznik_label12'
        i = 12

    if (pocet_otoc==2): 
      
        if (kliknute_pole[12] == 1) and ( kliknute_pole[11] ==1):
            otaznik_label12.after(ms=1000,func=lambda:otaznik_label12.config(image=HZfotka_tranzistor))   
            otaznik_label11.after(ms=1000,func=lambda:otaznik_label11.config(image=HZfotka_tranzistor_text))
            
        else:   
            otaznik_label12.after(ms=1000,func=lambda:otaznik_label12.config(image=HZfotka_otaznik0))
            eval(f"{prva}.after(ms=1000,func=lambda:{prva}.config(image=HZfotka_otaznik0))")
            kliknute_pole[12] = 0
            kliknute_pole[i] = 0 
            prva = ""
            i = 0
        pocet_otoc = 0
        ratanie +=1
        
def otacanie13(event):
    global prva,i,kliknute_pole,pocet_otoc,ratanie
    if (pocet_otoc<=2): 
        pocet_otoc = pocet_otoc + 1
        otaznik_label13.config(image=HZfotka_dc_source)
        kliknute_pole[13] = 1

    if pocet_otoc==1:
        prva = 'otaznik_label13'
        i = 13

    if (pocet_otoc==2): 
      
        if (kliknute_pole[13] == 1) and ( kliknute_pole[15] ==1):
            otaznik_label15.after(ms=1000,func=lambda:otaznik_label15.config(image=HZfotka_dc_source_text))   
            otaznik_label13.after(ms=1000,func=lambda:otaznik_label13.config(image=HZfotka_dc_source))
            
        else:   
            otaznik_label13.after(ms=1000,func=lambda:otaznik_label13.config(image=HZfotka_otaznik0))
            eval(f"{prva}.after(ms=1000,func=lambda:{prva}.config(image=HZfotka_otaznik0))")
            kliknute_pole[13] = 0
            kliknute_pole[i] = 0 
            prva = ""
            i = 0
        pocet_otoc = 0
        ratanie +=1
        
   

def otacanie14(event):
    global prva,i,kliknute_pole,pocet_otoc,ratanie
    if (pocet_otoc<=2): 
        pocet_otoc = pocet_otoc + 1
        otaznik_label14.config(image=HZfotka_rezistor_text)
        kliknute_pole[14] = 1

    if pocet_otoc==1:
        prva = 'otaznik_label14'
        i = 14

    if (pocet_otoc==2): 
      
        if (kliknute_pole[14] == 1) and ( kliknute_pole[5] ==1):
            otaznik_label14.after(ms=1000,func=lambda:otaznik_label14.config(image=HZfotka_rezistor_text))   
            otaznik_label05.after(ms=1000,func=lambda:otaznik_label05.config(image=HZfotka_rezistor))
            
        else:   
            otaznik_label14.after(ms=1000,func=lambda:otaznik_label14.config(image=HZfotka_otaznik0))
            eval(f"{prva}.after(ms=1000,func=lambda:{prva}.config(image=HZfotka_otaznik0))")
            kliknute_pole[14] = 0
            kliknute_pole[i] = 0 
            prva = ""
            i = 0
        pocet_otoc = 0
        ratanie +=1

def otacanie15(event):
    global pocet_otoc,ratanie,prva,i,kliknute15,kliknute13,kliknute_pole

    if (pocet_otoc<=2): 
        pocet_otoc = pocet_otoc + 1
        otaznik_label15.config(image=HZfotka_dc_source_text)
        kliknute_pole[15] = 1
        

    if pocet_otoc==1:
        prva = 'otaznik_label15'
        i = 15

    if (pocet_otoc==2): 
      
        if (kliknute_pole[15] == 1) and ( kliknute_pole[13] ==1):
            otaznik_label13.after(ms=1000,func=lambda:otaznik_label13.config(image=HZfotka_dc_source))
            otaznik_label15.after(ms=1000,func=lambda:otaznik_label15.config(image=HZfotka_dc_source_text))   
        else:   
            otaznik_label15.after(ms=1000,func=lambda:otaznik_label15.config(image=HZfotka_otaznik0))
            eval(f"{prva}.after(ms=1000,func=lambda:{prva}.config(image=HZfotka_otaznik0))")
            kliknute_pole[15] = 0
            kliknute_pole[i] = 0 
            
            prva = ""
            i = 0
        pocet_otoc = 0
        ratanie +=1

def konec(event):
    global ratanie
    if 0 not in kliknute_pole:
        messagebox.showinfo(title="pocet pokusov",message=f'pocet pokusov: {ratanie}')
        

fotka_ac_source_text = Image.open("AC_source_text.png")
Zfotka_ac_source_text = fotka_ac_source_text.resize((85,85))
HZfotka_ac_source_text = ImageTk.PhotoImage(Zfotka_ac_source_text)


fotka_ac_source = Image.open("AC_source.png")
Zfotka_ac_source = fotka_ac_source.resize((85,85))
HZfotka_ac_source = ImageTk.PhotoImage(Zfotka_ac_source)


fotka_kondenzator_text = Image.open("kondenzator_text.png")
Zfotka_kondenzator_text = fotka_kondenzator_text.resize((85,85))
HZfotka_kondenzator_text = ImageTk.PhotoImage(Zfotka_kondenzator_text)


fotka_kondenzator = Image.open("kondenzator.png")
Zfotka_kondenzator = fotka_kondenzator.resize((85,85))
HZfotka_kondenzator = ImageTk.PhotoImage(Zfotka_kondenzator)


fotka_dioda_text = Image.open("dioda_text.png")
Zfotka_dioda_text = fotka_dioda_text.resize((85,85))
HZfotka_dioda_text = ImageTk.PhotoImage(Zfotka_dioda_text)


fotka_dioda = Image.open("dioda.png")
Zfotka_dioda = fotka_dioda.resize((85,85))
HZfotka_dioda = ImageTk.PhotoImage(Zfotka_dioda)



fotka_cievka = Image.open("cievka.png")
Zfotka_cievka = fotka_cievka.resize((85,85))
HZfotka_cievka = ImageTk.PhotoImage(Zfotka_cievka)


fotka_cievka_text = Image.open("cievka_text.png")
Zfotka_cievka_text = fotka_cievka_text.resize((85,85))
HZfotka_cievka_text = ImageTk.PhotoImage(Zfotka_cievka_text)


fotka_rezistor_text = Image.open("rezistor_text.png")
Zfotka_rezistor_text = fotka_rezistor_text.resize((85,85))
HZfotka_rezistor_text = ImageTk.PhotoImage(Zfotka_rezistor_text)


fotka_rezistor = Image.open("rezistor.png")
Zfotka_rezistor = fotka_rezistor.resize((85,85))
HZfotka_rezistor = ImageTk.PhotoImage(Zfotka_rezistor)


fotka_transformator_text = Image.open("transformator_text.png")
Zfotka_transformator_text = fotka_transformator_text.resize((85,85))
HZfotka_transformator_text = ImageTk.PhotoImage(Zfotka_transformator_text)


fotka_transformator = Image.open("transformator.png")
Zfotka_transformator = fotka_transformator.resize((85,85))
HZfotka_transformator = ImageTk.PhotoImage(Zfotka_transformator)


fotka_tranzistor_text = Image.open("tranzistor_text.png")
Zfotka_tranzistor_text = fotka_tranzistor_text.resize((85,85))
HZfotka_tranzistor_text = ImageTk.PhotoImage(Zfotka_tranzistor_text)


fotka_tranzistor = Image.open("tranzistor.png")
Zfotka_tranzistor = fotka_tranzistor.resize((85,85))
HZfotka_tranzistor = ImageTk.PhotoImage(Zfotka_tranzistor)


fotka_dc_source = Image.open("DC_source.png")
Zfotka_dc_source = fotka_dc_source.resize((85,85))
HZfotka_dc_source = ImageTk.PhotoImage(Zfotka_dc_source)


fotka_dc_source_text = Image.open("DC_source_text.png")
Zfotka_dc_source_text = fotka_dc_source_text.resize((85,85))
HZfotka_dc_source_text = ImageTk.PhotoImage(Zfotka_dc_source_text)

 
fotka_otazik0 = Image.open("otaznik.png")
Zfotka_otaznik0 = fotka_otazik0.resize((85,85))
HZfotka_otaznik0 = ImageTk.PhotoImage(Zfotka_otaznik0)
otaznik_label0 = Label(root, image=HZfotka_otaznik0)
otaznik_label0.place(relx= 0.39, rely=0.3, anchor=CENTER)


otaznik_label01 = Label(root, image=HZfotka_otaznik0)
otaznik_label01.place(relx= 0.46, rely=0.3, anchor=CENTER)


otaznik_label02 = Label(root, image=HZfotka_otaznik0)
otaznik_label02.place(relx= 0.53, rely=0.3, anchor=CENTER)


otaznik_label03 = Label(root, image=HZfotka_otaznik0)
otaznik_label03.place(relx= 0.60, rely=0.3, anchor=CENTER)


otaznik_label04 = Label(root, image=HZfotka_otaznik0)
otaznik_label04.place(relx= 0.39, rely=0.43, anchor=CENTER)


otaznik_label05 = Label(root, image=HZfotka_otaznik0)
otaznik_label05.place(relx= 0.46, rely=0.43, anchor=CENTER)


otaznik_label06 = Label(root, image=HZfotka_otaznik0)
otaznik_label06.place(relx= 0.53, rely=0.43, anchor=CENTER)


otaznik_label07 = Label(root, image=HZfotka_otaznik0)
otaznik_label07.place(relx= 0.60, rely=0.43, anchor=CENTER)

otaznik_label08 = Label(root, image=HZfotka_otaznik0)
otaznik_label08.place( relx= 0.39, rely=0.56, anchor=CENTER)


otaznik_label09 = Label(root, image=HZfotka_otaznik0)
otaznik_label09.place(relx= 0.46, rely=0.56, anchor=CENTER)


otaznik_label10 = Label(root, image=HZfotka_otaznik0)
otaznik_label10.place(relx= 0.53, rely=0.56, anchor=CENTER)


otaznik_label11 = Label(root, image=HZfotka_otaznik0)
otaznik_label11.place(relx= 0.60, rely=0.56, anchor=CENTER)


otaznik_label12 = Label(root, image=HZfotka_otaznik0)
otaznik_label12.place(relx= 0.39, rely=0.69, anchor=CENTER)


otaznik_label13 = Label(root, image=HZfotka_otaznik0)
otaznik_label13.place(relx= 0.46, rely=0.69, anchor=CENTER)


otaznik_label14 = Label(root, image=HZfotka_otaznik0)
otaznik_label14.place(relx= 0.53, rely=0.69, anchor=CENTER)


otaznik_label15 = Label(root, image=HZfotka_otaznik0)
otaznik_label15.place(relx= 0.60, rely=0.69, anchor=CENTER)


otaznik_label0.bind('<Button-1>', otacanie0)
otaznik_label01.bind('<Button-1>', otacanie1)
otaznik_label02.bind('<Button-1>', otacanie2)
otaznik_label03.bind('<Button-1>', otacanie3)
otaznik_label04.bind('<Button-1>', otacanie4)
otaznik_label05.bind('<Button-1>', otacanie5)
otaznik_label06.bind('<Button-1>', otacanie6)
otaznik_label07.bind('<Button-1>', otacanie7)
otaznik_label08.bind('<Button-1>', otacanie8)
otaznik_label09.bind('<Button-1>', otacanie9)
otaznik_label10.bind('<Button-1>', otacanie10)
otaznik_label11.bind('<Button-1>', otacanie11)
otaznik_label12.bind('<Button-1>', otacanie12)
otaznik_label13.bind('<Button-1>', otacanie13)
otaznik_label14.bind('<Button-1>', otacanie14)
otaznik_label15.bind('<Button-1>', otacanie15)
root.bind('<Button-1>',konec)
  

root.mainloop()