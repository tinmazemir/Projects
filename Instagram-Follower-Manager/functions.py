from InstagramAPI import InstagramAPI
import getpass
import os


Followers = []
Following = []
FollowersClean = []
FollowingClean = []
Unfollowers = []
Unfollowing = []

def cleaner(CleaningList,CleanList):
	for i in CleaningList:
		if(i['username'] not in CleanList):
		   CleanList.append(i['username'])

def finder(UNF, Mode, FollowersClean, FollowingClean):
   if(Mode == "unfollowers"):
      for i in FollowingClean:
      	if((i not in FollowersClean) and (i not in UNF)):
      	   UNF.append(i)      	
   elif(Mode == "unfollowing"):
      for i in FollowersClean:
      	if((i not in FollowingClean) and (i not in UNF)):
      		UNF.append(i)
   else:
      print("You make mistake when give the arguments to finder.")

def process(Mode, UNF_For_finder, Followers_For_finder, Following_For_finder):
   global Followers,FollowersClean,Following,FollowingClean,Unfollowers,Unfollowing 
   if(Mode == "unfollowers"):
      finder(UNF=UNF_For_finder,Mode="unfollowers",FollowersClean=Followers_For_finder,FollowingClean=Following_For_finder)
      #print("UnfollowersList:"+str(UNF_For_finder))
   elif(Mode == "unfollowing"):     
      finder(UNF=UNF_For_finder,Mode="unfollowing",FollowersClean=Followers_For_finder,FollowingClean=Following_For_finder)
      #print("UnfollowingList:"+str(UNF_For_finder))
   else:
   	print("You make mistake when give the arguments to process.")

def finder_on_cmd():
   #user = input("username:")
   #password = getpass.getpass()
   
   #connecting to instagram
   #api = InstagramAPI(user,"password")
   api = InstagramAPI("tinmazemir","***")
   api.login()
   user_id = api.username_id
   print(user_id)
   os.system("cls")
   
   #taking data from instagram
   Followers = api.getTotalFollowers(user_id)
   Following = api.getTotalFollowings(user_id)
   
   cleaner(Followers,FollowersClean)
   cleaner(Following,FollowingClean)
   process(Mode= "unfollowers", UNF_For_finder= Unfollowers, Followers_For_finder= FollowersClean, Following_For_finder= FollowingClean)
   process(Mode= "unfollowing", UNF_For_finder= Unfollowing, Followers_For_finder= FollowersClean, Following_For_finder= FollowingClean)
   print("\nUnfollowers:"+str(len(Unfollowers)),"Unfollowing:"+str(len(Unfollowing)))




#finder_on_cmd()