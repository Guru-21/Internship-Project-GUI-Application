try:
    import Tkinter as tk
    import tkMessageBox as mb
    import numpy as np
    import matplotlib.pyplot as plt
    from tkinter import filedialog as fd
    from tkinter.messagebox import showinfo
except ImportError:
    import tkinter as tk
    import tkinter.messagebox as mb
    import numpy as np
    import matplotlib.pyplot as plt
    from tkinter import filedialog as fd
    from tkinter.messagebox import showinfo



#------------------------------------------------------------------------------------------------

root = tk.Tk()
root.title('GUI')
root.geometry("500x500")

tk.Label(root, text="PYTHON GUI", bg="goldenrod", font="bold").pack()
tk.Label(root, text="").pack()





#-----------------------------------------------------------------------------------------------------------------------
#data.py file part

def enterfile():
  inputFileName = fd.askopenfilename(title='Open a file')
  global new_file

  new_file = input('Enter the (.txt) file Name Where you want to store your data : ')

  showinfo(title='Selected File',message= 'Extracted data stored in : '+ new_file)

  count_total_line = 0

  inputFile = open(inputFileName, "r")

  for line in inputFile:

    count_total_line +=1
    line = line.strip().split()

    if ('Vmeas' in line) or ('Imeas' in line)  or ('V' in line):
      c1 = count_total_line
      break

  #new_file = 'test.txt'
  with open(new_file,'w') as nf:
    for line in inputFile:
      line = line.strip()
      nf.writelines(line)
      nf.write('\n')


    inputFile.close()
#-------------------------------------------------------------------------------------------------------------------------
#plot.py file


def plotgraph():

  data = np.loadtxt(new_file)

  x = data[:,0]
  y = data[:,1]

  #x, y = np.loadtxt('test.txt', unpack=True)   # you can do by the above two line like this
  plt.plot(x,y,'-bx')
  plt.title("Plot the v (x-axis) and i (y-axis)")
  plt.xlabel("voltage------>(v)")
  plt.ylabel("current------>(amp)")

  plt.show()



#-----------------------------------------------------------------------------------------------------------------------------------------------------
#parameter.py file part


def parameter():
  data = np.loadtxt(new_file)

  x = data[:, 0]
  y = data[:, 1]

  Vmeas=data[:,0]
  Imeas=data[:,1]


#power for i-th position

  powerlst=[]

  for i in range(len(x)):
    power = (Vmeas[i]*Imeas[i])
    powerlst.append(power)
  #print(power)    # power at i-th positions

# maximum power

  print("Maximum power(pmax) : ",max(powerlst))
  pmax = max(powerlst)

#volage value at pmax
  pmax_index = powerlst.index(pmax)

  print("voltage value at pmax : ",Vmeas[pmax_index])
  print("Current value at pmax : ",Imeas[pmax_index])





  mod_Vmeas = list()
  mod_Imeas = list()

#store Vmeas in mod_Vmeas
  for i in range(len(x)):
    mod_Vmeas.append(abs(Vmeas[i]))
# store Imeas in mod_Imeas
  for i in range(len(y)):
    mod_Imeas.append(abs(Imeas[i]))


  min_mod_Imeas = min(mod_Imeas)      # minimum value of mod_Imeas
  index_min_mod_Imeas = mod_Imeas.index(min_mod_Imeas)   # index of min_mod_Imeas
  print("Open-Circuit voltage (Voc) : ",Vmeas[index_min_mod_Imeas])


  min_mod_Vmeas = min(mod_Vmeas)     #minimum value of mod_Vmeas
  index_min_mod_Vmeas = mod_Vmeas.index(min_mod_Vmeas)     # index of min_mod_Vmeas
  print("Short-Circuit current (Isc) : ",Imeas[index_min_mod_Vmeas])







#-------------------------------------------------------------------------------------------------------------------------------------
#Button function calling part


tk.Button(root, text="Click for Enter File", bg="SkyBlue1", command=enterfile).pack()
tk.Label(root, text="").pack()

tk.Button(root, text="Click for Create Graph", bg="SkyBlue1", command=plotgraph).pack()
tk.Label(root, text="").pack()



tk.Button(root, text="Click for Check Some Parameter", bg="SkyBlue1", command=parameter).pack()

root.mainloop()