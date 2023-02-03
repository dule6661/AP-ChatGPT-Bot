from tkinter import *
import customtkinter
import openai
import os
import pickle

# Initiate App
root = customtkinter.CTk()
root.title("AP-ChatGPT Bot")
root.geometry('500x500')
root.iconbitmap('ai_lt.ico') #https://tkinter.com/ai_lt.ico

#Set Color Scheme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue") 

# Submit To AP-ChatGPT
def speak():
	if chat_entry.get():
		# Define our filename
		filename = "api_key"

		try:
			if os.path.isfile(filename):
				# Open the file
				input_file = open(filename, 'rb')

				#Load the data from the file into a variable
				var_stuff = pickle.load(input_file)

				# Query AP-ChatGPT
				# Define our API Key to AP-ChatGPT
				openai.api_key = var_stuff

				# Create an Instance
				openai.Model.list()

				# Define our Query / Response
				response = openai.Completion.create(
					model = "text-davinci-003",
					prompt = chat_entry.get(),
					temperature = 1,
					max_tokens = 600,
					top_p = 1.0,
					frequency_penalty = 0.0,
					presence_penalty = 0.0)

				my_text.insert(END, (response["choices"][0]["text"]).strip())
				my_text.insert(END, "\n\n")

			else:
				# Create the file
				input_file = open(filename, 'wb')
				# Close the file
				input_file.close()
				# Error message - you need an API key
				my_text.insert(END, "\n\nYou Need an API Key to talk with AP-ChatGPT. Get one here:\nhttps://beta.openai.com/acount/api-keys")

		except Exception as e:
			my_text.insert(END, f"\n\n There was an error\n\n{e}")	

	else:
		my_text.insert(END, "\n\nHey! You Forgot To Type Anything1")

# Clear the screans
def clear():
	# Clear The Main Text Box
	my_text.delete(1.0, END)

	# Clear the query entry widget
	chat_entry.delete(0, END)


# Do API Stuff
def key():

	# Define our filename
	filename = "api_key"

	try:
		if os.path.isfile(filename):
			# Open the file
			input_file = open(filename, 'rb')

			#Load the data from the file into a variable
			var_stuff = pickle.load(input_file)

			# Output var_stuff to our entry box
			api_entry.insert(END, var_stuff)
		else:
			# Create the file
			input_file = open(filename, 'wb')
			# Close the file
			input_file.close()

	except Exception as e:
		my_text.insert(END, f"\n\n There was an error\n\n{e}")		

	#Resize App Larger
	root.geometry('500x600')
	# Reshow API Frame	
	api_frame.pack(pady=30)

# Save The API Key
def save_key():
	# Define our filename
	filename = "api_key"

	try:
		# Open file
		output_file = open(filename, 'wb')
		# Actually add the data to the file
		pickle.dump(api_entry.get(), output_file)

		#Delete Entry box
		api_entry.delete(0, END)


		# Hide API Frame
		api_frame.pack_forget()
		# Resize App Smaller
		root.geometry('500x500')

	except Exception as e:
		my_text.insert(END, f"\n\n There was an error\n\n{e}")			

#Create Text Frame
text_frame = customtkinter.CTkFrame(root)
text_frame.pack(pady=20)

# Add Text Widget To Get ChatGPT Responses
my_text = Text(text_frame,
	bg="#343638",
	width=65,
	bd=1,
	fg="#d6d6d6",
	relief="flat",
	wrap=WORD,
	selectbackground="#1f538d")

my_text.grid(row=0, column=0)

# Create Scrollbar for text widget
text_scroll = customtkinter.CTkScrollbar(text_frame,
	command=my_text.yview)
text_scroll.grid(row=0, column=1, sticky="ns")

#Add the scrollbar to the textbox
my_text.configure(yscrollcommand=text_scroll.set)

# Entry Widget To Type Stuff to ChatGPT
chat_entry = customtkinter.CTkEntry(root,
	placeholder_text="Type Something To AP-ChatGPT...",
	width=435,
	height=50,
	border_width=1)
chat_entry.pack(pady=10)

#Create Button Frame
button_frame = customtkinter.CTkFrame(root, fg_color="#242424")
button_frame.pack(pady=20)

#Create Submit Buttons
submit_button = customtkinter.CTkButton(button_frame,
	text="Speak To AP-ChatGPT",
	command=speak)
submit_button.grid(row=0, column=0, padx=5)

#Create Clear Buttons
clear_button = customtkinter.CTkButton(button_frame,
	text="Clear Response",
	command=clear)
clear_button.grid(row=0, column=1, padx=5)

#Create API Key Buttons
api_button = customtkinter.CTkButton(button_frame,
	text="Update API Key",
	command=key)
api_button.grid(row=0, column=2, padx=5)

#Add API Key Frame
api_frame = customtkinter.CTkFrame(root, border_width=1)
api_frame.pack(pady=20)

#Add API Entry Widget
api_entry = customtkinter.CTkEntry(api_frame,
	placeholder_text="Enter Your API Key",
	width=280, height=50, border_width=1)
api_entry.grid(row=0, column=0, padx=5)

#Add API Save Button
api_save_button = customtkinter.CTkButton(api_frame,
	text="Save API Key",
	command=save_key)
api_save_button.grid(row=0, column=1, padx=10)




root.mainloop()
