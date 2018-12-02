import unittest
from tkinter import*
import random
from genetics import *

class User_interface:
    def __init__(self, window):
        self.window = window
        self.person1 = Person()
        self.person2 = Person()
        self.father_allele = StringVar()
        self.mother_allele = StringVar()
        
        self.fatherlabel = Label(window, text = "Father")
        self.fatherlabel.grid(row=0, column=0)
        self.motherlabel = Label(window, text= "Mother")
        self.motherlabel.grid(row =0, column = 1 )
        if True:
            self.person1.set_familial("Father")
            self.father_button1 = Radiobutton(window, text="Heterozygous",
                                     variable=self.father_allele, value='A,a')
            self.father_button1.grid(row= 1, column =0,sticky =W)
            self.father_button2 = Radiobutton(window, text = 'Homozygous Recessive', variable=self.father_allele , value='a,a')
            self.father_button2.grid(row=2, column = 0)
            self.father_button3 = Radiobutton(window, text='Homozygous Dominant', variable=self.father_allele, value ='A,A')
            self.father_button3.grid(row=3, column =0)
        if True:
            self.person2.set_familial("Mother")
            self.mother_button1 = Radiobutton(window, text="Heterozygous",
                                     variable=self.mother_allele, value='A,a')
            self.mother_button1.grid(row= 1, column =1, sticky = W)
            self.mother_button2 = Radiobutton(window, text = 'Homozygous Recessive', variable=self.mother_allele , value='a,a')
            self.mother_button2.grid(row=2, column = 1)
            self.mother_button3 = Radiobutton(window, text='Homozygous Dominant', variable=self.mother_allele, value ='A,A')
            self.mother_button3.grid(row=3, column =1)
        
        self.compute_button = Button(self.window, text="COMPUTE!", command = self.handlebutton)
        self.compute_button.grid(row = 4, column= 0, columnspan = 2)
        
        
        
    def handlebutton (self):
        ''' Clears screen and runs the prediction'''
        
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
        self.canvas = Canvas(self.window, width = 800,  height = 800, bg ='white')
        self.canvas.pack()
        
        #intializes the coordinates of the shapes
        self.x1 = 325
        self.y1 = 100
        self.x2 = 425
        self.y2 = 200
        
        #draws line between father square and mother circle
        self.canvas.create_line(self.x1+100, self.y1+40, self.x2+50, self.y1+40, fill="black")
        
      
        #creates a father square
        if (self.person1.get_allele()[0] + self.person1.get_allele()[1])== 'AA':
            self.canvas.create_rectangle(self.x1, self.y1,self.x2,self.y2) 
        elif (self.person1.get_allele()[0] + self.person1.get_allele()[1])=='Aa':
            self.canvas.create_rectangle(self.x1,self.y1, (self.x2)-50,self.y2)
            self.canvas.create_rectangle((self.x2)-50,self.y1, self.x2, self.y2, fill="black")
        else:
            self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill="black")
    
        
        #creates mother square
        if (self.person2.get_allele()[0] + self.person2.get_allele()[1]) == 'AA':
            self.canvas.create_oval(self.x1+150, self.y1,self.x2+150,self.y2)
        elif (self.person2.get_allele()[0] + self.person2.get_allele()[1]) == 'Aa':
            self.canvas.create_arc(self.x1+150, self.y1, self.x2+150, self.y2,extent = 180, start =90)
            self.canvas.create_arc(self.x1+150, self.y1, self.x2+150, self.y2, extent=180, start= 270, fill = "black")
        else:
            self.canvas.create_oval(self.x1+150, self.y1,self.x2+150,self.y2, fill = "black")
        count = 0
        
        #draws line to connect parents to kids
        self.canvas.create_line(200,300, 700, 300)
        self.canvas.create_line(450,140,450,300)
        
        self.gender_list = ['m','f']
        
        count= 0
        x1=150
        x2=250
        y1=350
        y2=450
        #draws kids on canvas
        for idx in range(len(self.predict.get_kids())):
            if self.predict.get_kids()[idx]== 'AA':
                if random.choice(self.gender_list) == 'm':
                    self.canvas.create_line(x1+50+count, y1-50,x2-50+count, y2-100)
                    self.canvas.create_rectangle(x1+count,y1,x2+count,y2)
                    self.canvas.create_text(x1+50 +count, y2 +50, text = str(self.predict.get_percent()[idx])+'%')
                else:
                    self.canvas.create_line(x1+50+count, y1-50,x2-50+count, y2-100)
                    self.canvas.create_oval(x1+count,y1,x2+count, y2)
                    self.canvas.create_text(x1+50 +count, y2 +50, text = str(self.predict.get_percent()[idx]) +'%')
                    
            
            #heterozygous child 
            elif self.predict.get_kids()[idx]== 'Aa':
                if random.choice(self.gender_list) == 'm':
                    self.canvas.create_line(x1+50+count, y1-50,x2-50+count, y2-100)
                    self.canvas.create_rectangle(x1 +count,y1, (x2-50)+count,y2)
                    self.canvas.create_rectangle((x2-50)+count,y1, x2 +count,y2, fill= 'black')
                    self.canvas.create_text(x1+50 +count, y2 +50, text = str(self.predict.get_percent()[idx]) +'%')
                    
                else:
                    self.canvas.create_line(x1+50+count, y1-50,x2-50+count, y2-100)
                    self.canvas.create_arc(x1 +count,y1, x2+count,y2, extent= 180, start=90)
                    self.canvas.create_arc(x1 +count,y1, x2+count,y2, extent= 180, start=270, fill='black')
                    self.canvas.create_text(x1+50 +count, y2 +50, text = str(self.predict.get_percent()[idx])+'%')
                
                
            else:
                if random.choice(self.gender_list) == 'm':
                    self.canvas.create_line(x1+50+count, y1-50,x2-50+count, y2-100)
                    #self.canvas.create_line(200,300,200,350+count)
                    self.canvas.create_rectangle(x1+count,y1,x2+count,y2, fill='black')
                    self.canvas.create_text(x1+50 +count, y2 +50, text = str(self.predict.get_percent()[idx])+'%')
                else:
                    self.canvas.create_line(x1+50+count, y1-50,x2-50+count, y2-100)
                    #self.canvas.create_line(200,300,200,350)
                    self.canvas.create_oval(x1+count,y1,x2+count, y2, fill = 'black')
                    self.canvas.create_text(x1+50 +count, y2 +50, text = str(self.predict.get_percent()[idx])+'%')
               
            count +=166
    
        
    
if __name__ == '__main__':
    root = Tk()
    root.title('Inheritance Prediction')
    app = User_interface(root)
    root.mainloop()    
