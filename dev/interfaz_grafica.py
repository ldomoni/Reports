from Tkinter import *
from acount import *    
from functools import partial
import os
import ttk

LINE_LABEL = None

def add_box_acount(name_acount, windows):
	name_acount = name_acount.capitalize()

	if not name_acount in LIST_ACOUNT_NAMES:
		
		for index, button in BUTTONS.iteritems():
			button.configure(state= NORMAL)
		LIST_ACOUNT_NAMES.append(name_acount)
		LIST_ACOUNT.append(Acount(name_acount))

		cbx['values'] = list(cbx['values']) + [name_acount]

		cbx.set(LIST_ACOUNT_NAMES[0])
		cbx.configure(width=10)
		cbx.grid(row=0, column=10)

	windows.destroy()

def window_add_acount():
	windows = Toplevel(root)
	windows.geometry('400x200')
	windows.title('Agregar cuenta')
	windows.configure(bg = 'beige')
	windows.focus_set()
	windows.grab_set()
	windows.transient(master=root)

	name_acount_label = Label(windows, text= 'Nombre de la cuenta', relief= 'ridge', borderwidth=5)
	name_acount_label.pack()

	name_acount_string = StringVar()
	name_acount_box = Entry(windows,textvariable=name_acount_string, relief= 'sunken', borderwidth=5)
	name_acount_box.pack()
	name_acount_box.focus()

	insert_button= Button(windows, text='Agregar cuenta', command= lambda :	add_box_acount(name_acount_string.get(), windows), anchor="w", relief= 'raised', borderwidth=5, activebackground = "Black", activeforeground="white")
	insert_button.pack()
	insert_button.bind('<Return>', partial(on_enter, insert_button))

	exit_button= Button(windows, text='Salir', command= windows.destroy, anchor="w", relief= 'raised', borderwidth=5, activebackground = "Black", activeforeground="white")
	exit_button.pack()
	exit_button.bind('<Return>', partial(on_enter, exit_button))

	windows.wait_window(window=windows)

def window_insert_delete():
	acount_name = cbx.get()
	acount = LIST_ACOUNT[LIST_ACOUNT_NAMES.index(acount_name)]

	windows = Toplevel(root)
	windows.geometry('400x250')
	windows.title('Agregar o eliminar item a la cuenta %s' %acount_name)
	windows.configure(bg = 'beige')
	windows.focus_set()
	windows.grab_set()
	windows.transient(master=root)

	description_label = Label(windows, text= 'Descripcion del item', relief= 'ridge', borderwidth=5)
	description_label.pack()

	description_string = StringVar()
	description_box = Entry(windows,textvariable=description_string, relief= 'sunken', borderwidth=5)
	description_box.pack()
	description_box.focus()

	amount_label = Label(windows, text= 'Monto del item', relief= 'ridge', borderwidth=5)
	amount_label.pack()

	amount_string = StringVar()
	amount_box = Entry(windows,textvariable=amount_string, relief= 'sunken', borderwidth=5)
	amount_box.pack()

	insert_button= Button(windows, text='Ingresar', command= lambda :[acount.add_item(description_string.get(), amount_string.get()), windows.destroy()], anchor="w", relief= 'raised', borderwidth=5, activebackground = "Black", activeforeground="white")
	insert_button.pack()
	insert_button.bind('<Return>', partial(on_enter, insert_button))

	delete_button= Button(windows, text='Eliminar', command= lambda :[acount.delete_item(description_string.get(), amount_string.get()), windows.destroy()], anchor="w", relief= 'raised', borderwidth=5, activebackground = "Black", activeforeground="white")
	delete_button.pack()
	delete_button.bind('<Return>', partial(on_enter, delete_button))

	exit_button= Button(windows, text='Salir', command= windows.destroy, anchor="w", relief= 'raised', borderwidth=5, activebackground = "Black", activeforeground="white")
	exit_button.pack()
	exit_button.bind('<Return>', partial(on_enter, exit_button))

	windows.wait_window(window=windows)

def window_report():
	acount_name = cbx.get()
	acount = LIST_ACOUNT[LIST_ACOUNT_NAMES.index(acount_name)]

	windows = Toplevel(root)
	windows.geometry('400x150')
	windows.title('generar reporte de la cuenta %s' %acount_name)
	windows.configure(bg = 'beige')
	windows.focus_set()
	windows.grab_set()
	windows.transient(master=root)

	try:
		acount.check_daily_exist()
		state_daily = NORMAL
	except:
		state_daily = DISABLED

	daily_report_button= Button(windows, text='Reporte diario', state= state_daily, command= lambda :[acount.daily_report(), windows.destroy()], anchor="w", relief= 'raised', borderwidth=5, activebackground = "Black", activeforeground="white")
	daily_report_button.pack()
	daily_report_button.bind('<Return>', partial(on_enter, daily_report_button))
	daily_report_button.focus()

	try:
		acount.check_month_open()
		state_month = NORMAL
	except:
		state_month = DISABLED

	month_report_button= Button(windows, text='Reporte mensual', state= state_month, command= lambda :[acount.month_report(), windows.destroy()], anchor="w", relief= 'raised', borderwidth=5, activebackground = "Black", activeforeground="white")
	month_report_button.pack()
	month_report_button.bind('<Return>', partial(on_enter, month_report_button))

	exit_button= Button(windows, text='Salir', command= windows.destroy, anchor="w", relief= 'raised', borderwidth=5, activebackground = "Black", activeforeground="white")
	exit_button.pack()
	exit_button.bind('<Return>', partial(on_enter, exit_button))


def on_enter(button, event):
	button.invoke()

def info(event):
	windows = Toplevel(root)
	windows.geometry('400x100')
	windows.title('Informacion de atajos')
	windows.configure(bg = 'beige')
	windows.focus_set()
	windows.grab_set()
	windows.transient(master=root)

	shortcuts_info_label = Label(windows, text= 'ctrl+indice: Ejecucion del boton. \n ctrl+q o ctrl+w: Salir de la aplicacion.', relief= 'ridge', borderwidth=5)
	shortcuts_info_label.pack()

	exit_button= Button(windows, text='Salir', command= windows.destroy, anchor="w", relief= 'raised', borderwidth=5, activebackground = "Black", activeforeground="white")
	exit_button.pack()
	exit_button.focus()
	exit_button.bind('<Return>', partial(on_enter, exit_button))

	windows.wait_window(window=windows)

def window_info_acount():
	acount_name = cbx.get()
	acount = LIST_ACOUNT[LIST_ACOUNT_NAMES.index(acount_name)]

	windows = Toplevel(root)
	windows.geometry('400x300')
	windows.title('Informacion de cuenta %s' %acount_name)
	windows.configure(bg = 'beige')
	windows.focus_set()
	windows.grab_set()
	windows.transient(master=root)

	info_label = Label(windows, text= acount.__repr__(), relief= 'ridge', borderwidth=5)
	info_label.pack()

	try:
		acount.repr_daily()
		state_daily = NORMAL
	except:
		state_daily = DISABLED

	daily_button= Button(windows, text='Informacion diaria', command= window_info_acount_daily, state=state_daily, anchor="w", relief= 'raised', borderwidth=5, activebackground = "Black", activeforeground="white")
	daily_button.pack()
	daily_button.focus()
	daily_button.bind('<Return>', partial(on_enter, daily_button))

	try:
		acount.repr_month()
		state_month = NORMAL
	except:
		state_month = DISABLED


	month_button= Button(windows, text='Informacion mensual', command= window_info_acount_month, state=state_month, anchor="w", relief= 'raised', borderwidth=5,activebackground = "Black", activeforeground="white")
	month_button.pack()
	month_button.focus()
	month_button.bind('<Return>', partial(on_enter, month_button))

	exit_button= Button(windows, text='Salir', command= windows.destroy, anchor="w", relief= 'raised', borderwidth=5, activebackground = "Black", activeforeground="white")
	exit_button.pack()
	exit_button.focus()
	exit_button.bind('<Return>', partial(on_enter, exit_button))

def window_info_acount_daily():
	acount_name = cbx.get()
	acount = LIST_ACOUNT[LIST_ACOUNT_NAMES.index(acount_name)]

	windows = Toplevel(root)
	windows.geometry('400x400')
	windows.title('Informacion de cuenta %s' %acount_name)
	windows.configure(bg = 'beige')
	windows.focus_set()
	windows.grab_set()
	windows.transient(master=root)

	info_label = Label(windows, text= acount.repr_daily(), relief= 'ridge', borderwidth=5)
	info_label.pack()

	exit_button= Button(windows, text='Salir', command= windows.destroy, anchor="w", relief= 'raised', borderwidth=5, activebackground = "Black", activeforeground="white")
	exit_button.pack()
	exit_button.focus()
	exit_button.bind('<Return>', partial(on_enter, exit_button))

def window_info_acount_month():
	acount_name = cbx.get()
	acount = LIST_ACOUNT[LIST_ACOUNT_NAMES.index(acount_name)]

	windows = Toplevel(root)
	windows.geometry('400x400')
	windows.title('Informacion de cuenta %s' %acount_name)
	windows.configure(bg = 'beige')
	windows.focus_set()
	windows.grab_set()
	windows.transient(master=root)

	info_label = Label(windows, text= acount.repr_month(), relief= 'ridge', borderwidth=5)
	info_label.pack()

	exit_button= Button(windows, text='Salir', command= windows.destroy, anchor="w", relief= 'raised', borderwidth=5, activebackground = "Black", activeforeground="white")
	exit_button.pack()
	exit_button.focus()
	exit_button.bind('<Return>', partial(on_enter, exit_button))

LIST_ACOUNT_NAMES= os.listdir(os.path.join(os.getcwd(), 'files'))
LIST_ACOUNT = []

for name in LIST_ACOUNT_NAMES:
	LIST_ACOUNT.append(Acount(name.capitalize()))

LIST_COMMAND = [
				('Agregar Cuenta', window_add_acount),
				('Agregar o eliminar item', window_insert_delete),
				('Generar Reporte', window_report),
				('Obtener informacion de cuenta', window_info_acount),
			
			]

BUTTONS = {}

root = Tk()

root.geometry('800x200') 
root.configure(bg = 'beige')
root.title('Aplicacion Reportes')

row=-1
column =0

 
cbx = ttk.Combobox(values=LIST_ACOUNT_NAMES)
if LIST_ACOUNT_NAMES:
	cbx.set(LIST_ACOUNT_NAMES[0])	


cbx.configure(width=10)
cbx.grid(row=0, column=10)

for pos in range(len(LIST_COMMAND)):
	command_name, command_button= LIST_COMMAND[pos]
	index_command = "%d%d" % (pos/10, pos%10)

	if row > 11:
		row = 0
		column= column+1
	else:
		row = row+1

	if (command_name == "Agregar Cuenta"):
		state_botton = NORMAL
	elif not LIST_ACOUNT_NAMES:
		state_botton = DISABLED
	
	command= Button(root, text=index_command + ')_ ' + command_name.capitalize(), state= state_botton, command= command_button, width=30, height=1, anchor="w", relief= 'raised', borderwidth=5, activebackground = "Black", activeforeground="white")
	command.grid(row= row, column= column)
	
	command.bind('<Return>', partial(on_enter,command))
	root.bind('<Control_L>%d%d' % (pos/10, pos%10), partial(on_enter, command))
	BUTTONS[index_command] = command

acount_label = Label(root, text= 'Cuenta a utilizar:', relief= 'ridge', borderwidth=5)
acount_label.grid(row=0, column=9)

button_exit= Button(root, text='Salir',command=root.destroy, relief= 'raised', borderwidth=5, activebackground = "Black", activeforeground="white")
button_exit.grid(row=1, column= 9)
button_exit.bind('<Return>', partial(on_enter, button_exit))
button_exit.focus()

root.bind('<Control-q>', partial(on_enter, button_exit))
root.bind('<Control-w>', partial(on_enter, button_exit))
root.bind('<Control-h>',info)

root.mainloop()
