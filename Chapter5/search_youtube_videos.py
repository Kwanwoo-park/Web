from apiclient.discovery import build

YOUTUBE_API_KEY = 'AIzaSyACVeMckmdr6Cet8A_pgvXVxkV6WddTqVk'

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

search_response = youtube.search().list(
    part='snippet',
    q='요리',
    type='video',
).execute()

for item in search_response['items']:
    print(item['snippet']['title'])