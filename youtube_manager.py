import json


def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_videos(videos):
    print("\n")
    print('*'*70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}.{video['name']},Duration: {video['time']}")
    print("\n")
    print('*'*70)    

def add_videos(videos):
    name=input("enter video name: ")
    time=input("enter video time: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)
def update_video(videos):
    list_videos(videos)
    index=int(input("enter video index to update: "))
    if 1 <= index <= len(videos):
        name=input("enter new video name: ")
        time=input("enter new video time: ")
        videos[index-1]={"name": name, "time": time}
        save_data_helper(videos)
    else:
        print("Invalid index. Please try again.")    
def remove_video(videos):
    list_videos(videos)
    index=int(input("enter video index to remove: "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid index. Please try again.")

def main():
    videos = load_data()
    while True:
        print("Youtube Manager || choose an option:")
        print("1. List videos")
        print("2. Add video")
        print("3. update video")
        print("4. Remove video")
        print("5. Exit")
        choice=input("Enter your choice: ")
       

        match choice:
            case "1":  
                list_videos(videos) 
            case "2":
                add_videos(videos)
            case "3":
                update_video(videos)
            case "4":
                remove_video(videos)
            case "5":
                print("Exiting...")
                break     
            case _:
                print("Invalid choice. Please try again.")     
if __name__ == "__main__":  
    main()              
    