from tkinter import *
from cv2 import *
class MyVideoCapture:
      def _init_(self,video_source=0):
      #open the video source
       self.vid=cv2.VideoCapture(video_source)
       if not self.vid.isOpened():
          raise ValueError("unable to open video source",video_source)
      #get video source width and height
      self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
      self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
      def get_frame(self):
          if self.vid.isOpened():
             ret,frame=self.vid.read()
             if ret:
                return(ret,cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
             else:
                 return (ret, None)
          else:
              return(ret,None)
#release the video source when the object is destroyed
      def _del_(self):
          if self.vid.isOpened():
             self.vid.release();
          self.window.mainloop()


     
class App:
    def _init_(self,window,window_title,video_source=0):
        self.window=window
        self.window.title(window_title)
        self.video_source=video_source
        # for opening the video source
        self.vid=MyVideoCapture(video_source)
        # create a canvas  that can fit the above video source size
        self.canvas=tkinter.Canvas(window,width=self.vid.width,height=self.vid.height)
self.canvas.pack()
self.window.mainloop()

window=tk.tk()
theLabel=Label(window,"click on the button to perform function")
topFrame = Frame(window)
topFrame.pack()
bottomFrame = Frame(window)
bottomFrame.pack(side=Toplevel)
button1 = Button(topFrame,text="1",fg="black")
button2 = Button(topFrame,text="2",fg="black")
button3 = Button(topFrame,text="3",fg="black")
button4 = Button(topFrame,text="4",fg="black")
button5 = Button(topFrame,text="5",fg="black")
button6 = Button(topFrame,text="6",fg="black")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
button5.pack(side=LEFT)
button6.pack(side=LEFT)

window.mainloop()
