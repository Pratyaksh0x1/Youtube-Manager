import sqlite3

from youtube_manager import save_data_helper
conn = sqlite3.connect('youtube_manager.db')
cursor = conn.cursor()

cursor.execute('''

CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL)''')
def load_data():
    cursor.execute("SELECT name, time FROM videos")
    rows = cursor.fetchall()
    videos = [{"name": row[0], "time": row[1]} for row in rows]
    return videos       
def save_data_helper(videos):
    cursor.execute("DELETE FROM videos")    
    for video in videos:
        cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (video["name"], video["time"]))
    conn.commit()
def list_videos():
    cursor.execute("SELECT name, time FROM videos")
    rows = cursor.fetchall()
    print("\n")
    print('*'*70)
    for index, row in enumerate(rows, start=1):
        print(f"{index}.{row[0]},Duration: {row[1]}")
    print("\n")
    print('*'*70)
def add_videos():
    name=input("enter video name: ")
    time=input("enter video time: ")
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()   
def update_video():
    list_videos()
    index=int(input("enter video index to update: "))
    cursor.execute("SELECT id FROM videos")
    rows = cursor.fetchall()
    if 1 <= index <= len(rows):
        name=input("enter new video name: ")
        time=input("enter new video time: ")
        video_id = rows[index-1][0]
        cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, video_id))
        conn.commit()
    else:
        print("Invalid index. Please try again.")   
def remove_video():
    list_videos()
    index=int(input("enter video index to remove: "))
    cursor.execute("SELECT id FROM videos")
    rows = cursor.fetchall()
    if 1 <= index <= len(rows):
        video_id = rows[index-1][0]
        cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
        conn.commit()
    else:
        print("Invalid index. Please try again.")   
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