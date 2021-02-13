from PIL import Image
import os 

images = {}

Path = "D:\\Code\\Projects\\Photo-Separated-by-Date\\test\\Monthly"

def load_images_from_folder(folder):
	f = open(folder+"\\ErrorFile.txt", "w")
	for filename in os.listdir(folder):
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
			
def copy_images_to_folder(target_folder, type = "M"):
	for img in images:
		#print(img+" -:- "+images[img])
		path_folder_name = images[img] 
		if(type == "M"):
			path_folder_name = path_folder_name.split(".")[:-1]
			path_folder_name = str(path_folder_name[0]+"."+path_folder_name[1])
			print(path_folder_name)
		
		if(os.path.exists(target_folder+'\\'+path_folder_name) == True):
			os.system(str("copy "+ img +"   "+target_folder+'\\'+path_folder_name))
		else:
			os.system("mkdir  "+target_folder+'\\'+path_folder_name)
			os.system(str("copy "+ img +"   "+target_folder+'\\'+path_folder_name))
			
def move_images_to_folder(target_folder, type = "M" ):
	for img in images:
		#print(img+" -:- "+path_folder_name)
		path_folder_name = images[img] 
		if(type == "M"):
			path_folder_name = path_folder_name.split(".")[:-1]
			path_folder_name = str(path_folder_name[0]+"."+path_folder_name[1])
			print(path_folder_name)

		if(os.path.exists(target_folder+'\\'+path_folder_name) == True):
			os.system(str("move "+ img +"   "+target_folder+'\\'+path_folder_name))
		else:
			os.system("mkdir  "+target_folder+'\\'+path_folder_name)
			os.system(str("move "+ img +"   "+target_folder+'\\'+path_folder_name))

def move_images_to_undated_folder(target_folder):
	if(os.path.isfile(target_folder+'\\'+"ErrorFile.txt") == True):
		undated = []
		f = open(target_folder+'\\'+"ErrorFile.txt","r")
		undated_check = f.readlines()
		f.close()
		#print(undated_check)
		for img in undated_check:
			#print(img)
			if(os.path.isdir(str(img)) == False):# \ tan dolayi isdir duzgun calisiyor klasor icindeki alt klasorleri de undated olarak isaretlip tasiyor 
				undated.append(img)	
		#print(undated)
		for img in undated:
			img = img[:-1]
			if(os.path.isdir(target_folder+'\\'+"Undated") == True):
				os.system(str("move "+ img +"   "+target_folder+'\\'+"Undated"))
			else:
				os.system("mkdir  "+target_folder+'\\'+"Undated")
				os.system("move "+ img +"   "+target_folder+'\\'+"Undated")


load_images_from_folder(Path)
#copy_images_to_folder(Path , "D")
move_images_to_folder(Path , "M")
move_images_to_undated_folder(Path)