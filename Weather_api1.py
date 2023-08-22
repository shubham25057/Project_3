import tkinter as tk
from PIL import Image,ImageTk
import requests

root=tk.Tk()

root.title("Weather App")
root.geometry("600x500")

def format_response(weather):
     try:
         city = weather['name']
         condition = weather['weather'][0]['description']
         temp = weather['main']['temp']
         final_str='city:%s\ncondtion:%s\nTemprature:%s'%(city,condition,temp)
     except:
         final_str='there wass a problem retrieving that information'
     return final_str


def get_weather(city):
    weather_key='56f8d51b2b25b087c5e111bdac186bda'
    url='https://api.openweathermap.org/data/2.5/weather'
    params={'APPID':weather_key,'q':city,'units':'imperial'}
    response= requests.get(url,params)

    weather=response.json()
    result['text']=format_response(weather)


heading_title=tk.Label(text='Earth over 200000 cities',fg='red',bg='sky blue',font=('times new roman',15,'bold'))
heading_title.place(x=80,y=18)

frame_one = tk.Frame(bg="blue",bd=5)
frame_one.place(x=80,y=60,width=450,height=50)

# Text box
txt_box = tk.Entry(frame_one,font=('times new roman',25),width=17)
txt_box.grid(row=0,column=0,sticky='w')

# Create button
btn = tk.Button(frame_one,text='get weather',fg='green',font=('times new roman',15,'bold'),command=lambda:get_weather(txt_box.get()))
btn.grid(row=0,column=1,padx=10)

frame_two = tk.Frame(bg="blue",bd=5)
frame_two.place(x=80,y=130,width=450,height=300)

result=tk.Label(frame_two,font=40,bg='white',justify='left',anchor='nw')
result.place(relwidth=1,relheight=1)

root.mainloop()