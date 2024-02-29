import streamlit as st

def display_videos():
    # Video URLs and corresponding titles (Replace these with actual video URLs and titles)
    video_info = [
        {"url": "D:\Abel\old_abel\Satwa\drug.mp4", "title": "Drug Addiction"},
        {"url": "D:\Abel\old_abel\Satwa\Love failure.mp4", "title": "Love Failure"},
        {"url": "D:\Abel\old_abel\Satwa\suicidal_Thought.mp4", "title": "Suicidal Thoughts"},
        {"url": "D:\Abel\old_abel\Satwa\loan.mp4", "title": "Loan"},
        {"url": "D:\Abel\old_abel\Satwa\Work_Stress.mp4", "title": "Work Stress"},
        {"url": "D:\Abel\old_abel\Satwa\exam.mp4", "title": "EXAM"}
    ]

    # Define number of columns in the grid
    num_columns = 3

    # Display videos with titles in a grid layout
    st.subheader("Success Stories")
    for i in range(0, len(video_info), num_columns):
        cols = st.columns(num_columns)
        for j in range(num_columns):
            index = i + j
            if index < len(video_info):
                with cols[j]:
                    st.video(video_info[index]['url'])
                    st.write(f"**{video_info[index]['title']}**")

def main():
    st.title("Rehabilitation Centre")
    display_videos()

if __name__ == "__main__":
    main()
