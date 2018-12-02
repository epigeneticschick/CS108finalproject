''' Lorrayya Williams with help from Professor Norman
Final Project: Genetic Heritablilty Prediction
CS 108
May 15, 2018 '''



import unittest
from tkinter import*
import random
from genetics import *

class User_interface:
    def __init__(self, window):
        self.window = window
        
        #intializes person 1
        self.person1 = Person()
        
        #intializes person 2
        self.person2 = Person()
        self.random_gender_list = []
        
       
        self.father_allele = StringVar()
        self.mother_allele = StringVar()
        
        #intializes possible genders
        self.gender_list = ['m','f']
        
        #creats father label
        self.fatherlabel = Label(window, text = "Father")
        self.fatherlabel.grid(row=0, column=0)
        
        #creates mother label 
        self.motherlabel = Label(window, text= "Mother")
        self.motherlabel.grid(row =0, column = 1 )
        
        
        #creates buttons to choose father's allele
        self.person1.set_familial("Father")
        self.father_button1 = Radiobutton(window, text="Heterozygous", variable=self.father_allele, value='A,a')
        self.father_button1.grid(row= 1, column =0,sticky =W)
        self.father_button2 = Radiobutton(window, text = 'Homozygous Recessive', variable=self.father_allele , value='a,a')
        self.father_button2.grid(row=2, column = 0)
        self.father_button3 = Radiobutton(window, text='Homozygous Dominant', variable=self.father_allele, value ='A,A')
        self.father_button3.grid(row=3, column =0)
        
            
        #creates buttons to choose mother's allele
        self.person2.set_familial("Mother")
        self.mother_button1 = Radiobutton(window, text="Heterozygous", variable=self.mother_allele, value='A,a')
        self.mother_button1.grid(row= 1, column =1, sticky = W)
        self.mother_button2 = Radiobutton(window, text = 'Homozygous Recessive', variable=self.mother_allele , value='a,a')
        self.mother_button2.grid(row=2, column = 1)
        self.mother_button3 = Radiobutton(window, text='Homozygous Dominant', variable=self.mother_allele, value ='A,A')
        self.mother_button3.grid(row=3, column =1)
        
        #button that draws genetic heritabilty
        self.compute_button = Button(self.window, text="COMPUTE!", command = self.handlebutton)
        self.compute_button.grid(row = 4, column= 0, columnspan = 2)
        
    def homozygous_dominant(self, x1,y1,x2, y2, list, count, idx, gender):
        '''Creates Homozygous Dominant Person'''
        if list[idx]== 'AA':
            if gender == 'm':
                self.canvas.create_rectangle(x1+count,y1,x2+count,y2)
            else:
                self.canvas.create_oval(x1+count,y1,x2+count, y2)
        
        
    def homozygous_recessive(self, x1, y1, x2, y2, list,count, idx, gender):
        '''Creates Homozygous Recessive Person'''
        if list[idx] == 'aa':
            if gender == 'm':
                self.canvas.create_rectangle(x1+count,y1,x2+count,y2, fill='black')
            else:
                self.canvas.create_oval(x1+count,y1,x2+count, y2, fill = 'black')
    
    def heterozygous (self,x1, y1, x2, y2, list, count, idx, gender):
        '''Creates Heterozygous Person'''
        if list[idx]== 'Aa':
            if gender == 'm':
                self.canvas.create_rectangle(x1 +count,y1, (x2-50)+count,y2)
                self.canvas.create_rectangle((x2-50)+count,y1, x2 +count,y2, fill= 'black')
                        
            else:
                self.canvas.create_arc(x1 +count,y1, x2+count,y2, extent= 180, start=90)
                self.canvas.create_arc(x1 +count,y1, x2+count,y2, extent= 180, start=270, fill='black')
        
    
    def create_generation(self,list,percent,x1,y1,x2,y2, random_gender = "default"):
    
        
        '''Creates a New Generation'''
        
        #allows programer to choose when genders are randomly chosen
        if random_gender != "default":
            self.random_gender_list = []
        
        #sets count to zero
        count = 0
        
        if self.random_gender_list == []:
            
            for idx in range(len(list)):
                
                #draws line that connects child
                self.canvas.create_line(x1+50+count, y1-50,x2-50+count, y2-100)
                
                #writes probablity of getting that allele
                self.canvas.create_text(x1+50 +count, y2 +50, text = str(percent[idx])+'%')
                
                
                #randomly chooses gender
                gender = random.choice(self.gender_list)
                
                #adds chosen geneder to the list 
                self.random_gender_list.append(gender)
                
                #draws homozygous dominant child
                self.homozygous_dominant(x1, y1,x2,y2, list,count,idx, gender)
                    
                #heterozygous child 
                self.heterozygous(x1, y1,x2,y2, list,count,idx, gender)
                #homozygous recessive child    
                self.homozygous_recessive(x1, y1,x2,y2, list,count, idx, gender)
                count +=166
            return
        
        else:
            for idx in range(len(list)):
            
            #draws line that connects child
                self.canvas.create_line(x1+50+count, y1-50,x2-50+count, y2-100)
                
                #writes probablity of getting that allele
                self.canvas.create_text(x1+50 +count, y2 +50, text = str(percent[idx])+'%')
                
                
                #randomly chooses gender
                gender = self.random_gender_list[idx]
                
                #adds chosen geneder to the list 
                self.random_gender_list.append(gender)
                
                #draws homozygous dominant child
                self.homozygous_dominant(x1, y1,x2,y2, list,count,idx, gender)
                    
                #heterozygous child 
                self.heterozygous(x1, y1,x2,y2, list,count,idx, gender)
                #homozygous recessive child    
                self.homozygous_recessive(x1, y1,x2,y2, list,count, idx, gender)
                count +=166
                
        
    def legend (self):
        ''' Creates Legend'''
        
        x1=10
        y1= 10
        x2=210
        y2= 275
        
        self.canvas.create_rectangle(x1,y1,x2,y2)
        self.canvas.create_text(x2-100, x1+20, text = "Legend")
        self.canvas.create_rectangle(x1+40,y1 +30,x1+80,y1 +70)
        self.canvas.create_text(x1 +60,x1+80, text = "Male")
        self.canvas.create_oval(x1+100,y1+30,x1+140,y1+70)
        self.canvas.create_text(x1 +120,y1 +80, text = "Female")
        self.canvas.create_oval(50,100,90,140)
        self.canvas.create_text(55,160, text = "Homozygous \n Dominant")
        self.canvas.create_rectangle(110,100,150,140, fill = "black")
        self.canvas.create_text(140,160, text = "Homozygous \n Recessive")
        self.canvas.create_arc(90,180,130,220, extent= 180, start =90)
        self.canvas.create_arc(90,180,130,220, extent =180, start =270, fill ='black')
        self.canvas.create_text(110,230, text ="Heterozygous")
        
        
    def draw_parents(self, person1,person2):
        '''Draws Parents'''
        self.canvas.create_line(self.x1+100, self.y1+40, self.x2+50, self.y1+40, fill="black")
        self.canvas.create_line(375,300, 875, 300)
        self.canvas.create_line(625,140,625,300)
        
        #creates father square
        if (person1[0] + person1[1])== 'AA':
            self.canvas.create_rectangle(self.x1, self.y1,self.x2,self.y2) 
        elif (person1[0] + person1[1])=='Aa':
            self.canvas.create_rectangle(self.x1,self.y1, (self.x2)-50,self.y2)
            self.canvas.create_rectangle((self.x2)-50,self.y1, self.x2, self.y2, fill="black")
        else:
            self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill="black")

    
        #creates mother circle
        if (person2[0] + person2[1]) == 'AA':
            self.canvas.create_oval(self.x1+150, self.y1,self.x2+150,self.y2)
        elif (person2[0] + person2[1]) == 'Aa':
            self.canvas.create_arc(self.x1+150, self.y1, self.x2+150, self.y2,extent = 180, start =90)
            self.canvas.create_arc(self.x1+150, self.y1, self.x2+150, self.y2, extent=180, start= 270, fill = "black")
        else:
            self.canvas.create_oval(self.x1+150, self.y1,self.x2+150,self.y2, fill = "black")
        count = 0

    def handlebutton (self):
        ''' Clears screen and runs the prediction'''
        #add legend
        
        
        #Clears all content on the window
        self.father_button1.destroy()
        self.father_button2.destroy()
        self.father_button3.destroy()
        self.mother_button1.destroy()
        self.mother_button2.destroy()
        self.mother_button3.destroy()
        self.compute_button.destroy()
        self.fatherlabel.destroy()
        self.motherlabel.destroy()
        
        #runs prediction
        self.person1.set_allele(self.father_allele.get())
        self.person2.set_allele(self.mother_allele.get())
        self.predict = Prediction()
        self.predict.set_alleles(self.person1.get_allele(), self.person2.get_allele())
        self.predict.probablity_kids()
        self.predict.capital_first()
        self.predict.percent_probability()
        
        #creates new canvas
        self.canvas = Canvas(self.window, width = 1200,  height = 800, bg ='white')
        self.canvas.grid(row=2, column= 1)
        
        self.Next_Generation_Button = Button(self.window, text= "Continue!", command = self.Next_Generation)
        self.Next_Generation_Button.grid(row=3, column=1)
        
        #intializes the coordinates of the shapes
        self.x1 = 500
        self.y1 = 100
        self.x2 = 600
        self.y2 = 200
        
        
        #draws legend
        self.legend()
        
        #draws line between father square and mother circle
        self.canvas.create_line(self.x1+100, self.y1+40, self.x2+50, self.y1+40, fill="black")
        
        self.draw_parents(self.person1.get_allele(),self.person2.get_allele())

        #draws kids on canvas
        self.create_generation(self.predict.get_kids(),self.predict.get_percent(),325,350,425,450)
        
       
    def Next_Generation(self):
        
        '''Button Creates SEcond Generation'''
        #destroys canvas and all buttons
        self.canvas.destroy()
        self.compute_button.destroy()
        self.Next_Generation_Button.destroy()
        
        #intialializes person 3
        
        self.person3 = Person()
        self.parent_allele = StringVar()
        
        if self.random_gender_list[0] == 'm':
            self.person3.set_familial("mother")
        else:
            self.person3.set_familial("father")
            
        self.parent_label = Label(self.window, text="What is the allele of the %s?" % self.person3.get_familial_relation())
        self.parent_label.grid(row=1, column =0)
        
        #button1
        self.parent_button1 = Radiobutton(self.window, text = 'Heteroyzygous', variable=self.parent_allele , value='A,a')
        self.parent_button1.grid(row =2, column =0)
        
        #button 2
        self.parent_button2 = Radiobutton(self.window, text = 'Homozygous Recessive', variable=self.parent_allele, value ='a,a')
        self.parent_button2.grid(row=3, column = 0)
        
        #button 3
        
        self.parent_button3 = Radiobutton(self.window, text = 'Homozygous Dominant', variable=self.parent_allele , value='A,A')
        self.parent_button3.grid(row =4,column =0)
        
#It setting allele to none  because self.parent is not getting the allele. FIX!!!!''' 
        
        #create a button to generate a third generation
        self.new_gen_button = Button(self.window, text='Next Generation', command =self.Third_Generation)
        self.new_gen_button.grid(row =5, column = 0, columnspan = 2)
        
    def Third_Generation(self):
        
        #sets person 3 allele
        self.person3.set_allele(self.parent_allele.get())
        
        #destroys everythin in frame
        self.parent_button1.destroy()
        self.parent_button2.destroy()
        self.parent_button3.destroy()
        self.new_gen_button.destroy()
        self.parent_label.destroy()
        
        #intalizes the fourth person
        self.person4 = Person()
        self.person4.set_allele(self.predict.add_comma(self.predict.get_kids()[0]))
        
        #intializes the second generation
        self.predict2 = Prediction()
        self.predict2.set_alleles(self.person3.get_allele(),self.person4.get_allele())
       
        
        
        self.predict2.probablity_kids()
        self.predict2.capital_first()
        self.predict2.percent_probability()
        self.canvas = Canvas(self.window, width = 1200,  height = 1000, bg ='white')
        self.canvas.grid(row=1, column= 1)
        
        #draws legend
        self.legend()
        
        
        #draws parents
        self.draw_parents(self.person1.get_allele(),self.person2.get_allele())
        
        #draws kids
        self.create_generation(self.predict.get_kids(),self.predict.get_percent(),325, 350,425,450)
        
        self.canvas.create_line(50,550,548,550)
        self.canvas.create_line(275,400,325,400)
        self.canvas.create_line(300,400,300,550)   
        
        
        #creates a father square 
        if self.person3.get_gender() == 'm':
            if (self.person3.get_allele()[0] + self.person3.get_allele()[1]) == "AA":
                self.canvas.create_rectangle(175,350,275,450)
            elif (self.person3.get_allele()[0] + self.person3.get_allele()[1]) == "Aa":
                self.canvas.create_rectangle(175,350, 225,450)
                self.canvas.create_rectangle(225,350, 275, 450, fill="black")
            else:
                self.canvas.create_rectangle(175,350,275,450, fill = "black")
       
       #creates a mother circle
        else:
            if (self.person3.get_allele()[0] + self.person3.get_allele()[1])== 'AA':
                self.canvas.create_oval(175,350,275,450)
            elif (self.person3.get_allele()[0] + self.person3.get_allele()[1]) == "Aa":
                self.canvas.create_arc(175, 350,275, 450,extent = 180, start =90)
                self.canvas.create_arc(175, 350, 275, 450, extent=180, start= 270, fill = "black")
            else:
                self.canvas.create_oval(175, 350,275,450, fill = "black")
                  
            
        
                  
            
        self.create_generation(self.predict2.get_kids(),self.predict2.get_percent(), 0,600,100,700, "New Genders")
        
        '''Complete the creation of second generation by drawing it on the Canvas.'''
        
        
        
    
if __name__ == '__main__':
    root = Tk()
    root.title('Inheritance Prediction')
    app = User_interface(root)
    root.mainloop()    
