import sqlite3

from youtube_manager import save_data_helper
conn = sqlite3.connect('youtube_manager.db')
cursor = conn.cursor()

cursor.execute('''

CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL)''')
def list_videos():
    cursor.execute("SELECT * FROM videos")
    for rows in cursor.fetchall():
     print(rows)
def add_videos():
    name=input("enter video name: ")
    time=input("enter video time: ")
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()   
def update_video():
    list_videos()
    video_id=int(input("enter video ID to update: "))
    name=input("enter new video name: ")
    time=input("enter new video time: ")
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, video_id))
    conn.commit()
def remove_video():
    list_videos()
    video_id=int(input("enter video ID to remove: "))
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()  
def main():
    while True:
        print("Youtube Manager with db || choose an option:")
        print("1. List videos")
        print("2. Add video")
        print("3. update video")
        print("4. Remove video")
        print("5. Exit")
        choice=input("Enter your choice: ")
       

        match choice:
            case "1":  
                list_videos() 
            case "2":
                add_videos()
            case "3":
                update_video()
            case "4":
                remove_video()
            case "5":
                print("Exiting...")
                break
    
    conn.close()
if __name__ == "__main__":
    main()