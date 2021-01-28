from PIL import Image
import os 

images = {}

Path = ""

def load_images_from_folder(folder):
	f = open(folder+"\\ErrorFile.txt", "w")
	for filename in os.listdir(folder):
		pass
		img = os.path.join(folder,filename)
		try:
			img_date = Image.open(os.path.join(folder,filename)).getexif()[36867].split()[0]
			img_date = img_date.replace(":",".")
			if img is not None:
				images[str(img)] = str(img_date)
		except:
			#print(img)
			f.write(img+'\n')
	f.close()
			
def copy_images_to_folder(target_folder):
	for img in images:
		#print(img+" -:- "+images[img])
		if(os.path.exists(target_folder+'\\'+images[img]) == True):
			os.system(str("copy "+ img +"   "+target_folder+'\\'+images[img]))
		else:
			os.system("mkdir  "+target_folder+'\\'+images[img])
			os.system(str("copy "+ img +"   "+target_folder+'\\'+images[img]))

def move_images_to_folder(target_folder):
	for img in images:
		#print(img+" -:- "+images[img])
		if(os.path.exists(target_folder+'\\'+images[img]) == True):
			os.system(str("move "+ img +"   "+target_folder+'\\'+images[img]))
		else:
			os.system("mkdir  "+target_folder+'\\'+images[img])
			os.system(str("move "+ img +"   "+target_folder+'\\'+images[img]))

def move_images_to_undated_folder(target_folder):
	if(os.path.isfile(target_folder+'\\'+"ErrorFile.txt") == True):
		undated = []
		f = open(target_folder+'\\'+"ErrorFile.txt","r")
		undated_check = f.readlines()
		f.close()
		#print(undated_check)
		for img in undated_check:
			if(os.path.isdir(img) == False):#Calismiyor
				undated.append(img)
		'''
		for i in undated:
			print(i[:-1])
		'''
		for img in undated:
			img = img[:-1]
			if(os.path.isdir(target_folder+'\\'+"Undated") == True):
				os.system(str("move "+ img +"   "+target_folder+'\\'+"Undated"))
			else:
				os.system("mkdir  "+target_folder+'\\'+"Undated")
				os.system("move "+ img +"   "+target_folder+'\\'+"Undated")
		
#load_images_from_folder(Path)
#copy_images_to_folder(Path)
#move_images_to_folder(Path)
#move_images_to_undated_folder(Path)