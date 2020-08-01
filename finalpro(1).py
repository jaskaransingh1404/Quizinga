from tkinter import *
from PIL import ImageTk,Image
import winsound
q1 = [
    "Q1.What was the RED KEEP's Chief Mouser called?",
    "Q2.Who fough the bear in S3?",
    "Q3.How many Kings/Queens did Lord Varys served?",
    "Q4.Who had the honour of kiling Petyr Baelish?",
    "Q5.What is name of Jon Snow's Direwolf?",
    "Q6.Who was known as QUEEN of Thorns?",
    "Q7.Who was the target practice in Joffrey's boudoir?",
    "Q8.Who was stabbed in the back by a smoke-baby ghost?",
    "Q9.How is SER DAVOS colloquially known?",
    "Q10.Who masterminded the plot to kill Joffrey?",
    "Q11.Where is the house of Black and White?",
    "Q12.What was the name of Fortune teller Cersei visited as a teenager?",
    "Q13.What is Lysa arryn's too-old-to-be-nursing son?",
    "Q14.What is the name of Arya’s sword?",
    "Q15.In which slum did Gendry grow up?"
]
options1 = [
    ["Ser Pounce 1","Master Paw","Lady Claws","Bastard"],
    ["Brienne 1","Jamie","Hound","Ghost"],
    ["2","3","4 1","5"],
    ["Jon Snow","Sansa Stark","Brienne","Arya Stark 1"],
    ["Grey WInd","Graham","Ghost 1","Lady"],
    ["Cersei Lannister","Olenna tyrell 1","Sansa Stark","Arya Stark"],
    ["Talisa Stark","Luwin","Ros 1","Maelcum Soul"],
    ["Qhorin Halfhand","Renly Baratheon 1","Jory Cassel","Tony Blackburn"],
    ["Potato Lord","Cabbage Duke","Onion Knight 1","Beetroot Lord"],
    ["Little Mix","Lord Varys","Olenna Tyrell 1","Rene Artois"],
    ["Qarth","Braavos 1","Meereen","No One Knows"],
    ["Jenny the Newt","Maggie the Frog 1","Winnie the Lizard","Kerry"],
    ["Edmore","Hoster","Robin 1","Nedwell"],
    ["Ice","Pointy","Fang","Needle 1"],
    ["Flea Bottom 1","Rat Bottom","Rhaenys's Hill","Dragonpit"]
]
a1 =[1,1,3,4,3,2,3,2,3,3,2,2,3,4,1]

q2 = [
    "Q1.Which country does Pete takes \nMonica for first date?",
    "Q2.What is Marcel's favorite song?",
    "Q3.Name the band which sang the title \nsong 'I'll Be There For You'",
    "Q4.Who quoted 'See, he’s her lobster.'",
    "Q5.What is Ross' first wife's name?",
    "Q6.What color is of Monica's apartment?",
    "Q7.What is the name of Ross and \nRachel's daughter?",
    "Q8.How many sisters does Joey have?",
    "Q9.What does Phoebe do for a living?",
    "Q10.What does Chandler's mom \ndo for a living?",
    "Q11.Who walks Phoebe down the aisle?",
    "Q12.Where does Rachel almost move \nat the end of the series?",
    "Q13.What do they call their neighbor \nacross the street?",
    "Q14.What does Ross do for a living?",
    "Q15.Where does Chandler's job \nget transferred?"
]
options2 = [
    ["England","Italy","France","Spain"],
    ["The Macarena","The Lion Sleeps Tonight","The Way\n You Look Tonight","My Heart \nWill Go On"],
    ["The Queens","U2","Oasis","The Rembrandts"],
    ["Monica","Ross","Rachel","Phoebe"],
    ["Susie","Carol","Emily","Susan"],
    ["Purple","Green","Yellow","White"],
    ["Emily","Emma","Vivianne","Elizabeth"],
    ["Five","Six","Seven","Eight"],
    ["Masseuse","Nurse","Teacher","Singer"],
    ["Author","Actress","Model","TV Host"],
    ["Ross","Gunther","Chandler","Joey"],
    ["Paris","Milan","California","Canada"],
    ["Naked Guy","Ugly Naked Guy","The Nudist","Naked \nNeighbor Guy"],
    ["Museum Curator","Scientist","Doctor","Paleontologist"],
    ["Ohia","Orlando","Long Island","Tulsa"]
]
a2 = [2, 2, 4, 4, 2, 1, 2, 3, 1, 1, 3, 1, 2, 4, 4]

q3 = [
    "Q1.What is Tony Stark's full name?",
    "Q2.Which song does Baby-Groot dance to in Post Credit of GotG 1?",
    "Q3.Who has never worn an IRON MAN suit?",
    "Q4.Which celebrity did Star-Lord named his ship after?",
    "Q5.What is Pepper Potts First Name?",
    "Q6.Who Assasinated Dr.Eriskine?",
    "Q7.What is Pepper Potts allergic to?",
    "Q8.What is the name of Ant-Man's Ant friend?",
    "Q9.What is the Wi-Fi password at KAMAR-TAJ?",
    "Q10.Who is Loki's Biological Father?",
    "Q11.M'Baku is the leader of which tribe?",
    "Q12.Who's the head of Dora Milaje?",
    "Q13.Who Attempts suicide in CA:Civil War?",
    "Q14.What is Red Skull's Real name?",
    "Q15.What is The Name of Rainbow Bridge of Asgard?"
]
options3= [
    ["Anthony Thomas Stark","Anthony Soprano Stark","Anthony Edward Stark","Anthony Ethan Stark"],
    ["Come and Get Your Love","Spirit in the Sky","Hooked on a Feeling","I Want You Back"],
    ["Pepper Potts","Happy Hogan","Bruce Bannner","James Rhodes"],
    ["Winona Ryder","Alyssa Milano","Demi Moore","Brooke Shields"],
    ["Virgina","Georgia","Josephine","Pepper"],
    ["Johann Schmidt","Jacques Dernier","Heingz Kruger","Dr.Zola"],
    ["Peaches","Peanuts","Strawberries 1 ","Tomatoes"],
    ["Ant-Thony","Ant-Tonio","Ant-Tonia","Ant-Tony"],
    ["Shamballa","Shambhala","Shangri-La","Endgame"],
    ["Laufey","Odin","Bor","Raze"],
    ["Golden","Jabari","Mining","River"],
    ["Okoye","Shuri","Nakia","Ramonda"],
    ["Sharon Carter","James Rhodes","Helmut Zemo","Bucky Barnes"],
    ["Johann Wanger","Johann Eriskine","Johann Newcastle","Johann Schmidt"],
    ["Bifrost","Sakaar","Ragnarok","Mjlonir"]
]
a3 = [3,4,2,2,1,3,3,1,1,1,2,1,3,4,1]

q4 = [
    "Q1.How did Joffrey die?",
    "Q2.Who was Sansa never married to?",
    "Q3.Which one isn't Daenerys's dragons?",
    "Q4.Which is not Daenerys's titles?",
    "Q5.Which kingdom is furthest south?",
    "Q6.What is the sigil of house Baratheon?",
    "Q7.How are Jon and Daenerys related \nto each other?",
    "Q8.Who did Brienne of Tarth lose her \nvirginity to?",
    "Q9.Where would you find the Citadel?",
    "Q10.Who created the Night King?",
    "Q11.What is the birth name of HODOR?",
    "Q12.Who said: 'I don’t plan on knitting \nby the fire while men fight for me'?",
    "Q13.Who did Euron murder to \ntake the SALT THRONE?",
    "Q14.What is the name of Arya’s sword?",
    "Q15.In which slum did Gendry grow up?"
]
options4 = [
    ["Poisoned at his own wedding feast" ,"Struck by an errant crossbow shot" ,"Stabbed by a horde of small children ","Thrown from the walls of the Red Keep"],
    ["Tyrion Lannister" ,"Loras Tyrell ","Joffrey Baratheon ","Ramsay Bolton"],
    ["Rhaegal" ,"Aegon" ,"Viserion" ,"Drogon"],
    ["The Unsullied" ,"Breaker of Chains" ,"Khaleesi ","Mother of Dragons"],
    ["The Vale ","Dorne ","The Reach" ,"The Riverlands"],
    ["Stag ","Rose" ,"Unicorn" ,"Moon"],
    ["Cousins" ,"They arent ","Aunt  nephew","Brother sister"],
    ["Margaery Tyrell" ,"Tormund Giantsbane" ,"Jaime Lannister" ,"Renly Baratheon"],
    ["Lannisport" ,"Qarth ","Oldtown" ,"Braavos"],
    ["The Lord of Light","The Children of the Forest","The Drowned God","The First Men"],
    ["Wylis","Horys","Myrys","Gladys"],
    ["Lyanna Mormont","Sansa Stark","Ser Brienne of Tarth","Olenna Tyrell"],
    ["His brother","His uncle","His nephew","His cousin"],
    ["Ice","Pointy","Fang","Needle"],
    ["Flea Bottom","Rat Bottom","Rhaenys’s Hill","Dragonpit"]
]
a4 = [1, 2 ,2 ,1 ,2 ,1 ,3 ,3 ,2, 2, 2, 1, 1, 4, 1]
class Quiz1:
    def __init__(self, master):
        self.opt_selected = IntVar()
        self.qn = 0
        self.correct = 0
        self.ques = self.create_q(master, self.qn)
        self.opts = self.create_options(master, 4)
        self.display_q(self.qn)
        #self.button = Button(master, text="Back", bg="red",command=self.back_btn)
        #self.button.place(x=260,y=725)
        #self.button = Button(master, text="Next", bg="lime green",command=self.next_btn)
        #self.button.place(x=260,y=700)
        #self.button = Button(master, text="tell score", bg="cyan",command=self.print_results)
        #self.button.place(x=250,y=752)

    def player():
        play()
        
    def create_q(self, master, qn):
        w = Label(master,text=str(qn)+q1[qn],bg="grey32",fg="snow",font=("trajan",25))
        w.place(x=150,y=3)
        return w

    def create_options(self, master, n):
        b_val = 0
        b = []
        while b_val < n:
            btn = Radiobutton(master, text="foo",indicatoron=0,font=("trajan",16), bg="grey32",fg="snow",height=2,width=40,variable=self.opt_selected, value=b_val+1,command=self.next_btn)
            b.append(btn)
            btn.place(x=150,y=60*b_val+200, anchor="w")
            b_val = b_val + 1
        return b

    def display_q(self, qn):
        b_val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q1[qn]
        for op in options1[qn]:
            self.opts[b_val]['text'] = op
            b_val = b_val + 1

    def check_q(self, qn):
        if self.opt_selected.get() == a1[qn]:
            return True
        return False

    def print_results(self):
        root.destroy()
        root3=Tk()
        root3.geometry("500x600")
        print("Score: ", self.correct, "/", len(q1))
        b="Score: "+str(self.correct)+"/"+str(len(q1))
        ourMessage =b
        messageVar = Message(text = ourMessage) 
        messageVar.config(bg='lightgreen') 
        messageVar.pack( )
        x=self.correct
        if x==len(q1):
            b="DIE hard Fan."
        elif x<len(q1) and x>=10:
            b="Quiet a part of true fan club."
        else:
            b="You just saw it once."
        ourMessage=b
        messageVar = Message(text = ourMessage,font=()) 
        messageVar.config(bg='lightgreen') 
        messageVar.pack( )
        x=self.correct
        
    def back_btn(self):
        print("go back")
        self.qn=self.qn-1
        self.correct -=1
        self.display_q(self.qn)

    def next_btn(self):
        if self.check_q(self.qn):
            print("Correct")
            self.correct += 1
        else:
            print("Wrong")
        self.qn = self.qn + 1
        if self.qn >= len(q1):
            self.print_results()
        else:
            self.display_q(self.qn)


class Quiz2:
    def __init__(self, master):
        self.opt_selected = IntVar()
        self.qn = 0
        self.correct = 0
        self.ques = self.create_q(master, self.qn)
        self.opts = self.create_options(master, 4)
        self.display_q(self.qn)
        #self.button = Button(master, text="Back",bg="red" ,command=self.back_btn)
        #self.button.place(x=510,y=725)
        #self.button = Button(master, text="Skip",bg="lime green" ,command=self.next_btn)
        #self.button.place(x=510,y=700)
        #self.button = Button(master, text="tell score",bg="cyan" ,command=self.print_results)
        #self.button.place(x=500,y=752)


    def create_q(self, master, qn):
        w = Label(master, text=str(qn)+q2[qn],font=("dafont",25),bg="mediumOrchid1",fg="gray1")
        w.place(x=150,y=3)
        return w

    def create_options(self, master, n):
        b_val = 0
        b = []
        while b_val < n:
            btn = Radiobutton(master, text="foo",indicatoron=0,font=("trajan",16), bg="mediumOrchid1",fg="gray1",height=2,width=40,variable=self.opt_selected, value=b_val+1,command=self.next_btn)
            b.append(btn)
            btn.place(x=150,y=60*b_val+190, anchor="w")
            b_val = b_val + 1
        return b

    def display_q(self, qn):
        b_val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q2[qn]
        for op in options2[qn]:
            self.opts[b_val]['text'] = op
            b_val = b_val + 1

    def check_q(self, qn):
        if self.opt_selected.get() == a2[qn]:
            return True
        else:
            return False
        return true
    def print_results(self):
        root.destroy()
        root3=Tk()
        root3.geometry("500x600")
        print("Score: ", self.correct, "/", len(q2))
        b="Score: "+str(self.correct)+"/"+str(len(q2))
        ourMessage =b
        messageVar = Message(text = ourMessage) 
        messageVar.config(bg='lightgreen') 
        messageVar.pack( )
        x=self.correct
        if x==len(q2):
            b="DIE hard Fan."
        elif x<len(q2) and x>=10:
            b="Quiet a part of true fan club."
        else:
            b="You just saw it once."
        ourMessage=b
        messageVar = Message(text = ourMessage,font=25) 
        messageVar.config(bg='lightgreen') 
        messageVar.pack( )
        x=self.correct
        

    def back_btn(self):
        print("go back")
        self.qn=self.qn-1
        self.correct -=1
        self.display_q(self.qn)

    def next_btn(self):
        if self.check_q(self.qn):
            print("Correct")
            self.correct += 1
        else:
            print("Wrong")
        self.qn = self.qn + 1
        if self.qn >= len(q2):
            self.print_results()
        else:
            self.display_q(self.qn)
    
class Quiz3:
    def __init__(self, master):
        self.opt_selected = IntVar()
        self.qn = 0
        self.correct = 0
        self.ques = self.create_q(master, self.qn)
        self.opts = self.create_options(master, 4)
        self.display_q(self.qn)
        #self.button = Button(master, text="Back", bg="red",command=self.back_btn)
        #self.button.place(x=260,y=725)
        #self.button = Button(master, text="Next", bg="lime green",command=self.next_btn)
        #self.button.place(x=260,y=700)
        #self.button = Button(master, text="tell score", bg="cyan",command=self.print_results)
        #self.button.place(x=250,y=752)

    def player():
        play()
        
    def create_q(self, master, qn):
        w = Label(master,text=str(qn)+q3[qn],bg="grey32",fg="snow",font=("trajan",25))
        w.place(x=150,y=3)
        return w

    def create_options(self, master, n):
        b_val = 0
        b = []
        while b_val < n:
            btn = Radiobutton(master, text="foo",indicatoron=0,font=("trajan",16), bg="grey32",fg="snow",height=2,width=40,variable=self.opt_selected, value=b_val+1,command=self.next_btn)
            b.append(btn)
            btn.place(x=150,y=60*b_val+200, anchor="w")
            b_val = b_val + 1
        return b

    def display_q(self, qn):
        b_val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q3[qn]
        for op in options3[qn]:
            self.opts[b_val]['text'] = op
            b_val = b_val + 1

    def check_q(self, qn):
        if self.opt_selected.get() == a3[qn]:
            return True
        return False

    def print_results(self):
        root.destroy()
        root3=Tk()
        root3.geometry("500x600")
        print("Score: ", self.correct, "/", len(q3))
        b="Score: "+str(self.correct)+"/"+str(len(q3))
        ourMessage =b
        messageVar = Message(text = ourMessage) 
        messageVar.config(bg='lightgreen') 
        messageVar.pack( )
        x=self.correct
        if x==len(q3):
            b="DIE hard Fan."
        elif x<len(q3) and x>=10:
            b="Quiet a part of true fan club."
        else:
            b="You just saw it once."
        ourMessage=b
        messageVar = Message(text = ourMessage,font=()) 
        messageVar.config(bg='lightgreen') 
        messageVar.pack( )
        x=self.correct
        
    def back_btn(self):
        print("go back")
        self.qn=self.qn-1
        self.correct -=1
        self.display_q(self.qn)

    def next_btn(self):
        if self.check_q(self.qn):
            print("Correct")
            self.correct += 1
        else:
            print("Wrong")
        self.qn = self.qn + 1
        if self.qn >= len(q3):
            self.print_results()
        else:
            self.display_q(self.qn)

class Quiz4:
    def __init__(self, master):
        self.opt_selected = IntVar()
        self.qn = 0
        self.correct = 0
        self.ques = self.create_q(master, self.qn)
        self.opts = self.create_options(master, 4)
        self.display_q(self.qn)
        #self.button = Button(master, text="Back", bg="red",command=self.back_btn)
        #self.button.place(x=260,y=725)
        #self.button = Button(master, text="Next", bg="lime green",command=self.next_btn)
        #self.button.place(x=260,y=700)
        #self.button = Button(master, text="tell score", bg="cyan",command=self.print_results)
        #self.button.place(x=250,y=752)
    def create_q(self, master, qn):
        w = Label(master,text=str(qn)+q4[qn],bg="grey32",fg="snow",font=("trajan",25))
        w.place(x=150,y=3)
        return w

    def create_options(self, master, n):
        b_val = 0
        b = []
        while b_val < n:
            btn = Radiobutton(master, text="foo",indicatoron=0,font=("trajan",16), bg="grey32",fg="snow",height=2,width=40,variable=self.opt_selected, value=b_val+1,command=self.next_btn)
            b.append(btn)
            btn.place(x=150,y=60*b_val+200, anchor="w")
            b_val = b_val + 1
        return b

    def display_q(self, qn):
        b_val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q4[qn]
        for op in options4[qn]:
            self.opts[b_val]['text'] = op
            b_val = b_val + 1

    def check_q(self, qn):
        if self.opt_selected.get() == a4[qn]:
            return True
        return False

    def print_results(self):
        root.destroy()
        root3=Tk()
        root3.geometry("500x600")
        print("Score: ", self.correct, "/", len(q4))
        b="Score: "+str(self.correct)+"/"+str(len(q4))
        ourMessage =b
        messageVar = Message(text = ourMessage) 
        messageVar.config(bg='lightgreen') 
        messageVar.pack( )
        x=self.correct
        if x==len(q4):
            b="DIE hard Fan."
        elif x<len(q1) and x>=10:
            b="Quiet a part of true fan club."
        else:
            b="You just saw it once."
        ourMessage=b
        messageVar = Message(text = ourMessage,font=()) 
        messageVar.config(bg='lightgreen') 
        messageVar.pack( )
        x=self.correct
        
    def back_btn(self):
        print("go back")
        self.qn=self.qn-1
        self.correct -=1
        self.display_q(self.qn)

    def next_btn(self):
        if self.check_q(self.qn):
            print("Correct")
            self.correct += 1
        else:
            print("Wrong")
        self.qn = self.qn + 1
        if self.qn >= len(q4):
            self.print_results()
        else:
            self.display_q(self.qn)




root=Tk()
root.geometry("780x540")

def des():
    label.destroy()
    b1.destroy()
    b2.destroy()

def play():
    winsound.PlaySound('got.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
def play1():
    winsound.PlaySound('friends.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
def play2():
    winsound.PlaySound('avengers.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
def play3():
    winsound.PlaySound('hedwigs.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
def friend():
    play1()
    load = Image.open("friens.jpg")
    render = ImageTk.PhotoImage(load)
    img = Label(image=render)
    img.image = render
    img.place(x=0,y=0)
    app1=Quiz2(root)
    root.configure(bg='plum1')
    root.geometry("780x540")
    des()
def got():
    play()
    load = Image.open("got.jpg")
    render = ImageTk.PhotoImage(load)
    img = Label(image=render)
    img.image = render
    img.place(x=0, y=0)
    app2=Quiz1(root)
    root.configure(bg='orangered4')
    root.geometry("780x540")
    des()
def mcu():
    play2()
    load = Image.open("avengers.jpg")
    render = ImageTk.PhotoImage(load)
    img = Label(image=render)
    img.image = render
    img.place(x=0, y=0)
    app3=Quiz3(root)
    root.configure(bg='orangered4')
    root.geometry("780x540")
    des()
def hp():
    play3()
    load = Image.open("harry.jpg")
    render = ImageTk.PhotoImage(load)
    img = Label(image=render)
    img.image = render
    img.place(x=0, y=0)
    app4=Quiz4(root)
    root.configure(bg='orangered4')
    root.geometry("780x540")
    des()

root.configure(bg='black')
label=Label(text="Select topic of quiz",font=("Algerian",54),fg="turquoise2",bg="gray26")
label.pack()
b1=Button(text="FRIENDS",font=("dafont",32),width=30,fg='turquoise2',bd=0,bg='gray26',activebackground='black',activeforeground='white',relief=FLAT,cursor='hand2',command=friend)
b2=Button(text="Game Of Thrones",font=("Trajan",32),width=30,fg='turquoise2',bd=0,bg='gray26',activebackground='black',activeforeground='white',relief=FLAT,cursor='hand2',command=got)
b3=Button(text="Marvel Universe",font=("Trajan",32),width=30,fg='turquoise2',bd=0,bg='gray26',activebackground='black',activeforeground='white',relief=FLAT,cursor='hand2',command=mcu)
b4=Button(text="Harry Potter",font=("Trajan",32),width=30,fg='turquoise2',bd=0,bg='gray26',activebackground='black',activeforeground='white',relief=FLAT,cursor='hand2',command=hp)
b1.place(x=10,y=150)
b2.place(x=10,y=240)
b3.place(x=10,y=330)
b4.place(x=10,y=420)



'''
app1 = Quiz1(root1)
app2 = Quiz2(root1)
'''
