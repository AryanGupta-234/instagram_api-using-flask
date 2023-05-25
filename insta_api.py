from instagrapi import Client
from apscheduler.schedulers.background import BackgroundScheduler
import json
from instagrapi.exceptions import ClientLoginRequired

# create an instance of the client class
user_name=""
pass_word=""
# username = "mad_codes"
# password = "hacked9243"
import time


def login(username="None" ,password= "None"):
    global client,user_name,pass_word
    client = Client( )

    
    # client.dump_settings('dump.json')
    try:
        with open('dump.json', 'r') as f:
            settings = json.load(f)
           
        print(f)
        try:
            if settings['username']==username and settings['password'] == password:
                client.load_settings('dump.json')
                client.login(username, password)
                user_name=username
                pass_word=password
                print("fast")
                return True
            else:
                try:
                    client.login(username, password)
                    
                   
                    client.dump_settings('dump.json')
                    with open('dump.json', 'r') as f:
                        settings = json.load(f)
                    settings['username'] = username
                    settings['password'] = password
                    user_name=username
                    pass_word=password
                    with open('dump.json', 'w') as f:
                        json.dump(settings, f)
                    print("Slow")
                    return True
           
                except Exception as e:
                    print("fst",username,password)
                    print(e)
        except Exception as e:
            print(e)
            print("fst2",username,password)

    except FileNotFoundError:
        try:
            client.login(username, password)
            client.dump_settings('dump.json')
            with open('dump.json', 'r') as f:
                settings = json.load(f)
            settings['username'] = username
            settings['password'] = password
            user_name=username
            pass_word=password
            with open('dump.json', 'w') as f:
                json.dump(settings, f)               
            return True
        except Exception as e:
            print(e)
            print("fst3",username,password)




 
login("mad_codes","hacked9243")
def upload_reel(path,caption="",hashtags=""):
    # upload a reel
    # reel_path = input("enter ur path to media ").replace('"','')
    print(user_name,pass_word,"er")
    # login(user_name,pass_word)
    reel_path=path.replace('"','')
    # try:
    client.clip_upload(reel_path, caption)
    print("Reel posted successfully!")
    # except Exception as e:
    # print("Could not post reel:", e)

 




def down_reel(url):
    # initializing download
    try:
        print()
        url= client.media_info( client.media_pk_from_url(url)).dict()
        views = url.get("view_count")
        captions = url.get("caption_text", "")
        likes = url.get("like_count")
        username = url.get("username")
        full_name = url.get("full_name")
        duration = url.get("video_duration")
        urls = url.get("video_url")
        tags=url.get("user_tags")
        tags=[]
        caption=[]
        for i in captions.split(" "):
            if i.startswith("#") or i.startswith(".#") or i.startswith("\n\n.\n#")  :
                tags.append(i.replace("\n",""))
            else:
                caption.append(i.replace("\n",""))
        client.clip_download_by_url(urls, folder="C:\\Users\\aassw\\Downloads")
    except Exception as e:
        print(e)


def test():
    print("hello")

def scheduler(link,hours,status=False):
    # down_reel(link)
    print(status)
    # schedule_date = datetime.datetime(2023, 5, 10, 12, 0, 0) # replace with your scheduled date
    # schedule.every().day.at(schedule_date.strftime('%H:%M')).do(upload_reel, reel_path, caption)
    schedule.every().day.at("07:18").do( test)


# login to Instagram "mad_codes" "hacked9243"
# username = str(input("enter ur username "))
# password = str(input("enter ur password "))


#



# schedule.every(10).seconds.do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(60)



