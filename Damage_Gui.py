from tkinter import *
import json

class GUI(object):
    def __init__(self):
        self.Root = Tk()
        self.Canvas_Root = Canvas(self.Root)
        self.Canvas_Root.pack(expand=True,fill=BOTH)
        
        self.Numbers = json.load(open('Config.json'))
        
        self.Category_Options = [x for x in self.Numbers['Category']]
        self.Category_Selected = IntVar()
        self.Category_Selected.set(1)
        self.Category_Selected.trace('w',self.Damage_Update)
        self.Level_Selected = StringVar()
        self.Level_Selected.set("1")
        self.Level_Selected.trace('w',self.Damage_Update)
        self.Attack_Value =StringVar()
        self.Attack_Value.set("0")
        self.Attack_Value.trace('w',self.Damage_Update)
        self.Rarity_Options = [x for x in self.Numbers['Rarity']]
        self.Rarity_Selected = StringVar()
        self.Rarity_Selected.set('Common')
        self.Rarity_Selected.trace('w',self.Damage_Update)
        self.Rank_Options = [x for x in self.Numbers['Rank']]
        self.Rank_Selected = StringVar()
        self.Rank_Selected.set('Unranked')
        self.Rank_Selected.trace('w',self.Damage_Update)
        self.Perk_Amount = StringVar()
        self.Perk_Amount.set("0")
        self.Perk_Amount.trace('w',self.Damage_Update)
        self.Winstance_Status = IntVar()
        self.Winstance_Status.trace('w',self.Damage_Update)
        self.Arena_Boost_1_Value = StringVar()
        self.Arena_Boost_1_Value.set("0")
        self.Arena_Boost_1_Status = IntVar()
        self.Arena_Boost_2_Value = StringVar()
        self.Arena_Boost_2_Value.set("0")
        self.Arena_Boost_2_Status = IntVar()
        self.Misc_Status = IntVar()
        self.Misc_Value = StringVar()
        self.Misc_Value.set("0")
        self.Saved_History_Input_Output = [StringVar() for x in range(self.Numbers['History Length'])]
        self.Empowerment_Selected = IntVar()
        self.Empowerment_Options = [0,1,2,3,4,5]
        self.Arena_Boost_1_Value.trace('w',self.Damage_Update)
        self.Arena_Boost_1_Status.trace('w',self.Damage_Update)
        self.Arena_Boost_2_Value.trace('w',self.Damage_Update)
        self.Arena_Boost_2_Status.trace('w',self.Damage_Update)
        self.Misc_Status.trace('w',self.Damage_Update)
        self.Misc_Value.trace('w',self.Damage_Update)
        self.Empowerment_Selected.trace('w',self.Damage_Update)
        
        self.row_gap = 40
        self.title_row = 20
        self.header_row = self.title_row + self.row_gap
        self.entry_row = self.header_row + self.row_gap
        self.damage_row = self.entry_row + self.row_gap+30
        self.history_row = self.damage_row + self.row_gap
        
        self.column_gap = 75
        self.category_column = 50
        self.level_column = self.category_column + self.column_gap
        self.attack_column = self.level_column + self.column_gap+15
        self.rarity_column = self.attack_column + self.column_gap+25
        self.empowerment_column = self.rarity_column + self.column_gap+35
        self.rank_column = self.empowerment_column + self.column_gap+35
        self.perk_column = self.rank_column + self.column_gap+45
        self.bonus1_column = self.perk_column + self.column_gap+65
        self.bonus2_column = self.bonus1_column + self.column_gap+90
        
        self.Canvas_Root.create_text(self.category_column,self.header_row,text='Category')
        self.Canvas_Root.create_text(self.level_column,self.header_row,text='Level')
        self.Canvas_Root.create_text(self.attack_column,self.header_row,text='Attack Damage')
        self.Canvas_Root.create_text(self.rarity_column,self.header_row,text='Rarity')
        self.Canvas_Root.create_text(self.empowerment_column,self.header_row,text='Stars/Grade')
        self.Canvas_Root.create_text(self.rank_column,self.header_row,text='Rank')
        self.Canvas_Root.create_text(self.perk_column,self.header_row,text='Damage Perks')
        self.Canvas_Root.create_text(int((self.bonus1_column+self.bonus2_column)/2),self.header_row,text='Other Bonuses')
        
        self.category_menu =OptionMenu(self.Root,self.Category_Selected,*self.Category_Options)
        self.Canvas_Root.create_window(self.category_column,self.entry_row,window=self.category_menu,width=50)
        self.category_menu.configure(indicatoron=False)
        self.Canvas_Root.create_window(self.level_column,self.entry_row,window=Entry(self.Root,textvariable=self.Level_Selected,justify=CENTER),width=40)
        self.Canvas_Root.create_window(self.attack_column,self.entry_row,window=Entry(self.Root,textvariable=self.Attack_Value,justify=CENTER),width=60)
        
        self.rarity_menu =OptionMenu(self.Root,self.Rarity_Selected,*self.Rarity_Options)
        self.Canvas_Root.create_window(self.rarity_column,self.entry_row,window=self.rarity_menu,width=75)
        self.rarity_menu.configure(indicatoron=False)
        
        self.empowerment_menu = OptionMenu(self.Root,self.Empowerment_Selected,*self.Empowerment_Options)
        self.Canvas_Root.create_window(self.empowerment_column,self.entry_row,window=self.empowerment_menu,width=50)
        self.empowerment_menu.configure(indicatoron=False)
        
        self.rank_menu =OptionMenu(self.Root,self.Rank_Selected,*self.Rank_Options)
        self.Canvas_Root.create_window(self.rank_column,self.entry_row,window=self.rank_menu,width=100)
        self.rank_menu.configure(indicatoron=False)
        self.Canvas_Root.create_window(self.perk_column,self.entry_row,window=Entry(self.Root,textvariable=self.Perk_Amount,justify=CENTER),width=40)
        
        self.entry_row_upper_adjust = self.entry_row-15
        self.entry_row_lower_adjust = self.entry_row+15
        
        self.Canvas_Root.create_window(self.bonus1_column-20,self.entry_row_upper_adjust,window=Checkbutton(self.Root,text="Arena Boost: ",variable=self.Arena_Boost_1_Status))
        self.Canvas_Root.create_window(self.bonus1_column+45,self.entry_row_upper_adjust,window=Entry(self.Root,textvariable=self.Arena_Boost_1_Value,justify=CENTER),width=30)
        self.Canvas_Root.create_text(self.bonus1_column+67,self.entry_row_upper_adjust,text="%")
        
        self.Canvas_Root.create_window(self.bonus2_column-20,self.entry_row_upper_adjust,window=Checkbutton(self.Root,text="Arena Boost: ",variable=self.Arena_Boost_2_Status))
        self.Canvas_Root.create_window(self.bonus2_column+45,self.entry_row_upper_adjust,window=Entry(self.Root,textvariable=self.Arena_Boost_2_Value,justify=CENTER),width=30)
        self.Canvas_Root.create_text(self.bonus2_column+67,self.entry_row_upper_adjust,text="%")
        
        self.Canvas_Root.create_window(self.bonus1_column-13,self.entry_row_lower_adjust,window=Checkbutton(self.Root,text="Winstance (20%)",variable=self.Winstance_Status))
        
        self.Canvas_Root.create_window(self.bonus2_column-20,self.entry_row_lower_adjust,window=Checkbutton(self.Root,text="Misc Boost: ",variable=self.Misc_Status))
        self.Canvas_Root.create_window(self.bonus2_column+45,self.entry_row_lower_adjust,window=Entry(self.Root,textvariable=self.Misc_Value,justify=CENTER),width=30)
        self.Canvas_Root.create_text(self.bonus2_column+67,self.entry_row_lower_adjust,text="%")
        
        self.Root_Height = self.history_row+self.row_gap
        self.Root_Width = self.bonus2_column+self.column_gap+87
        
        self.Canvas_Root.create_text(int(self.Root_Width/2),20,text="Damage Calculator (non-skills)",font='Helvecita 20 bold underline')
        self.Damage_Display = self.Canvas_Root.create_text(int(self.Root_Width/2),self.damage_row,text="Damage: 0 [range: 0 - 0]",font="Helvecita 20 bold")
        self.Damage_Update()
        
        self.ws = self.Root.winfo_screenwidth() # width of the screen
        self.hs = self.Root.winfo_screenheight() # height of the screen
        self.x = int((self.ws/2) - (self.Root_Width/2))
        self.y = int((self.hs/2) - (self.Root_Height/2))
        self.Root.geometry(f"{self.Root_Width}x{self.Root_Height}+{self.x}+{self.y}")
        self.Root.mainloop()
        
    def Damage_Update(self,*args):
        Entry_Values = [self.Attack_Value.get(),self.Level_Selected.get(),self.Misc_Value.get(),self.Perk_Amount.get(),self.Arena_Boost_1_Value.get(),self.Arena_Boost_2_Value.get()]
        if "" in Entry_Values:
            for count,x in enumerate(Entry_Values):
                if x == "":
                    Entry_Values[count] = "0"
        Damage = (self.Numbers['Category'][str(self.Category_Selected.get())]*(int(Entry_Values[1])**1.5+10)/250+int(Entry_Values[0]))*1.5*(1+self.Numbers['Rarity'][self.Rarity_Selected.get()]*self.Empowerment_Selected.get()+float(self.Numbers['Rank'][self.Rank_Selected.get()])+self.Arena_Boost_1_Status.get()*int(Entry_Values[4])/100+self.Arena_Boost_2_Status.get()*int(Entry_Values[5])/100+self.Winstance_Status.get()*.2+self.Misc_Status.get()*int(Entry_Values[2])/100+int(Entry_Values[3])*.03)
        self.Canvas_Root.itemconfigure(self.Damage_Display,text=f"Damage: {int(Damage)} [Range: {int(.9*Damage)} - {int(1.2*Damage)}]")

GUI()