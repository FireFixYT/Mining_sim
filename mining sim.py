import random
from tkinter import *

root=Tk()
root.title("Mine Simulator")
root.geometry("500x500")
root.resizable(False, False)

ores=["stone","coal","copper","iron","lapis","gold","diamond","titan"]
cost=[1,2,7,20,45,100,225,450]
cost_multi=[1,2,3,4,5,6,7,8]
power_cost_upgrade=[250,750,2500,8000,20000,65000,125000,None]
range_cost_upgrade=[1000,5000,20000,75000,150000,300000,600000,1000000,None]
final_cost=[2500000,0]
chance=[[[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[0,200],[200,550],[550,1000]], [[-1,-1],[-1,-1],[-1,-1],[-1,-1],[0,100],[100,350],[350,650],[650,1000]], [[-1,-1],[-1,-1],[-1,-1],[0,100],[100,250],[250,450],[450,700],[700,1000]], [[-1,-1],[-1,-1],[0,100],[100,250],[250,400],[400,550],[550,750],[750,1000]], [[-1,-1],[0,70],[70,190],[190,320],[320,460],[460,620],[620,800],[800,1000]], [[0,90],[90,190],[190,300],[300,420],[420,550],[550,690],[690,850],[850,1000]], [[0,170],[170,320],[320,460],[460,590],[590,710],[710,820],[820,920],[920,1000]], [[0,270],[270,410],[410,540],[540,660],[660,760],[760,850],[850,930],[930,1000]]]

class drill():
    upgr=""
    ore=""
    money=0
    chance=0
    ore_in_moment=0
    drill_power=0
    drill_range=0
    stone=0
    coal=0
    copper=0
    iron=0
    lapis=0
    gold=0
    diamond=0
    titan=0
    invent=[titan,diamond,gold,lapis,iron,copper,coal,stone]
    def __init__(self, drill_power, drill_range):
        self.drill_power=drill_power
        self.drill_range=drill_range
    def update_ores(self):
        c.itemconfigure(stone_col,text=f"{self.invent[7]}")
        c.itemconfigure(coal_col,text=f"{self.invent[6]}")
        c.itemconfigure(copper_col,text=f"{self.invent[5]}")
        c.itemconfigure(iron_col,text=f"{self.invent[4]}")
        c.itemconfigure(lapis_col,text=f"{self.invent[3]}")
        c.itemconfigure(gold_col,text=f"{self.invent[2]}")
        c.itemconfigure(diamond_col,text=f"{self.invent[1]}")
        c.itemconfigure(titan_col,text=f"{self.invent[0]}")
        c.itemconfigure(money_txt,text=f"Money={self.money}$")
    def dril(self):
        self.ore_in_moment=self.drill_range
        for d in range(self.ore_in_moment):
            self.chance=random.randint(1,1000) 
            for j in range(8):
                if self.chance>chance[self.drill_power][j][0] and self.chance<=chance[self.drill_power][j][1]:
                    self.invent[j]+=1
        pi.update_ores()
    def sell_stone(self):
        self.money+=pi.invent[7]*cost[0]
        self.invent[7]=0
        pi.update_ores()
    def sell_coal(self):
        self.money+=pi.invent[6]*cost[1]
        self.invent[6]=0
        pi.update_ores()    
    def sell_copper(self):
        self.money+=pi.invent[5]*cost[2]
        self.invent[5]=0
        pi.update_ores()
    def sell_iron(self):
        self.money+=pi.invent[4]*cost[3]
        self.invent[4]=0
        pi.update_ores()     
    def sell_lapis(self):
        self.money+=pi.invent[3]*cost[4]
        self.invent[3]=0
        pi.update_ores()
    def sell_gold(self):
        self.money+=pi.invent[2]*cost[5]
        self.invent[2]=0
        pi.update_ores()    
    def sell_diamond(self):
        self.money+=pi.invent[1]*cost[6]
        self.invent[1]=0
        pi.update_ores()
    def sell_titan(self):
        self.money+=pi.invent[0]*cost[7]
        self.invent[0]=0
        pi.update_ores()    
    def upgrade_power(self):
        if (power_cost_upgrade[self.drill_power]!=None) and (self.money>=power_cost_upgrade[self.drill_power]):
            self.money=self.money-power_cost_upgrade[self.drill_power]
            self.drill_power+=1
        c.itemconfigure(money_txt,text=f"Money={self.money}$")
        c.itemconfigure(power_txt,text=f"Drill Power={self.drill_power}")
        c.itemconfigure(upgrade_power_txt,text=f"Upgrade Power Cost={power_cost_upgrade[self.drill_power]}$")
    def upgrade_range(self):
        if (range_cost_upgrade[self.drill_range-1]!=None) and (self.money>=range_cost_upgrade[self.drill_range-1]):
            self.money=self.money-range_cost_upgrade[self.drill_range-1]
            self.drill_range+=1
        c.itemconfigure(money_txt,text=f"Money={self.money}$")
        c.itemconfigure(range_txt,text=f"Drill Range={self.drill_range}")
        c.itemconfigure(upgrade_range_txt,text=f"Upgrade Range Cost={range_cost_upgrade[self.drill_range-1]}$")    
    def final(self):
        if self.money>=final_cost[0]:
            self.money-=final_cost[0]
            c.itemconfigure(money_txt,text=f"Money={self.money}$")
            c.itemconfigure(final_txt,text=f"Thanks for playing")
            final_button.place(x=800,y=800)
            drill_button.place(x=800,y=800)
            sell_stone.place(x=800,y=800)
            sell_coal.place(x=800,y=800)
            sell_copper.place(x=800,y=800)
            sell_iron.place(x=800,y=800)
            sell_lapis.place(x=800,y=800)
            sell_gold.place(x=800,y=800)
            sell_diamond.place(x=800,y=800)
            sell_titan.place(x=800,y=800)
            upgrade_power.place(x=800,y=800)
            upgrade_range.place(x=800,y=800)
            c.itemconfigure(money_txt,text=f"Thanks for playing")
            c.itemconfigure(upgrade_range_txt,text=f"Thanks for playing")
            c.itemconfigure(upgrade_power_txt,text=f"Thanks for playing")
            c.itemconfigure(range_txt,text=f"Thank You")
            c.itemconfigure(power_txt,text=f"Thank You")
            c.itemconfigure(stone_col,text=f"Thx")
            c.itemconfigure(coal_col,text=f"Thx")
            c.itemconfigure(copper_col,text=f"Thx")
            c.itemconfigure(iron_col,text=f"Thx")
            c.itemconfigure(lapis_col,text=f"Thx")
            c.itemconfigure(gold_col,text=f"Thx")
            c.itemconfigure(diamond_col,text=f"Thx")
            c.itemconfigure(titan_col,text=f"Thx")  
            c.itemconfigure(stone_txt,text=f"Thx")
            c.itemconfigure(coal_txt,text=f"Thx")
            c.itemconfigure(copper_txt,text=f"Thx")
            c.itemconfigure(iron_txt,text=f"Thx")
            c.itemconfigure(lapis_txt,text=f"Thx")
            c.itemconfigure(gold_txt,text=f"Thx")
            c.itemconfigure(diamond_txt,text=f"Thx")
            c.itemconfigure(titan_txt,text=f"Thx")             

pi=drill(0,1)

c=Canvas(width=500,height=500,bg='white')
c.pack()

stone_col=c.create_text(30,10,text=f"{pi.stone}",justify=CENTER, font="Verdana 12") 
coal_col=c.create_text(90,10,text=f"{pi.coal}",justify=CENTER, font="Verdana 12")
copper_col=c.create_text(150,10,text=f"{pi.copper}",justify=CENTER, font="Verdana 12")
iron_col=c.create_text(210,10,text=f"{pi.iron}",justify=CENTER, font="Verdana 12")
lapis_col=c.create_text(270,10,text=f"{pi.lapis}",justify=CENTER, font="Verdana 12")
gold_col=c.create_text(330,10,text=f"{pi.gold}",justify=CENTER, font="Verdana 12")
diamond_col=c.create_text(400,10,text=f"{pi.diamond}",justify=CENTER, font="Verdana 12")
titan_col=c.create_text(470,10,text=f"{pi.titan}",justify=CENTER, font="Verdana 12")

final_txt=c.create_text(250,205,text=f"Final cost = {final_cost[0]}$",justify=LEFT, font="Verdana 13")
upgrade_power_txt=c.create_text(375,145,text=f"Upgrade Power Cost={power_cost_upgrade[0]}$",justify=RIGHT, font="Verdana 12")
upgrade_range_txt=c.create_text(127,145,text=f"Upgrade Range Cost={range_cost_upgrade[0]}$",justify=LEFT, font="Verdana 12")
power_txt=c.create_text(425,85,text=f"Drill Power={pi.drill_power}",justify=LEFT, font="Verdana 12")
range_txt=c.create_text(75,85,text=f"Drill Range={pi.drill_range}",justify=LEFT, font="Verdana 12")
money_txt=c.create_text(250,85,text=f"Money={pi.money}$",justify=LEFT, font="Verdana 12")
stone_txt=c.create_text(30,30,text=f"stone",justify=CENTER, font="Verdana 12") 
coal_txt=c.create_text(90,30,text=f"coal",justify=CENTER, font="Verdana 12")
copper_txt=c.create_text(150,30,text=f"copper",justify=CENTER, font="Verdana 12")
iron_txt=c.create_text(210,30,text=f"iron",justify=CENTER, font="Verdana 12")
lapis_txt=c.create_text(270,30,text=f"lapis",justify=CENTER, font="Verdana 12")
gold_txt=c.create_text(330,30,text=f"gold",justify=CENTER, font="Verdana 12")
diamond_txt=c.create_text(400,30,text=f"diamond",justify=CENTER, font="Verdana 12")
titan_txt=c.create_text(470,30,text=f"titan",justify=CENTER, font="Verdana 12")

drill_button=Button(text="Drill",font=("Arial",47),command=pi.dril)
c.create_window(250,375,window=drill_button,width=175,height=75)
pi.ores="stone"
sell_stone=Button(text="sell",font=("Arial",15),command=pi.sell_stone)
c.create_window(30,55,window=sell_stone,width=50,height=25)
sell_coal=Button(text="sell",font=("Arial",15),command=pi.sell_coal)
c.create_window(90,55,window=sell_coal,width=50,height=25)
sell_copper=Button(text="sell",font=("Arial",15),command=pi.sell_copper)
c.create_window(150,55,window=sell_copper,width=50,height=25)
sell_iron=Button(text="sell",font=("Arial",15),command=pi.sell_iron)
c.create_window(210,55,window=sell_iron,width=50,height=25)
sell_lapis=Button(text="sell",font=("Arial",15),command=pi.sell_lapis)
c.create_window(270,55,window=sell_lapis,width=50,height=25)
sell_gold=Button(text="sell",font=("Arial",15),command=pi.sell_gold)
c.create_window(330,55,window=sell_gold,width=50,height=25)
sell_diamond=Button(text="sell",font=("Arial",15),command=pi.sell_diamond)
c.create_window(400,55,window=sell_diamond,width=50,height=25)
sell_titan=Button(text="sell",font=("Arial",15),command=pi.sell_titan)
c.create_window(470,55,window=sell_titan,width=50,height=25)
upgrade_power=Button(text="Upgrade Power Drill",font=("Arial",14),command=pi.upgrade_power)
c.create_window(405,115,window=upgrade_power,width=175,height=30)
upgrade_range=Button(text="Upgrade Range Drill",font=("Arial",14),command=pi.upgrade_range)
c.create_window(95,115,window=upgrade_range,width=175,height=30)
final_button=Button(text="Final Button",font=("Arial",14),command=pi.final)
c.create_window(250,175,window=final_button,width=110,height=30)
root.mainloop()