from pytubefix import YouTube

def DescargarMP3(url, carpeta=None):
  try:
    video = YouTube(url)
    download = video.streams.get_audio_only()
    if(carpeta):
      download.download(output_path=carpeta)
    else:
      download.download()
      
    return 1
  except Exception as e:
    return 0
  
  
if __name__ == "__main__":
  DescargarMP3("https://www.youtube.com/watch?v=YQ-qToZUybM", "C:\\Users\\Lalitho_\\Downloads")