from django.shortcuts import render
from .forms import VideoForm

# Create your views here.

def create_video(request):
	if request.method == 'POST':
		form = VideoForm(request.POST, request.FILES) 
		if form.is_valid():
			video = form.save(commit=False)	# Crea la variable video sin guardarla en la base de datos aún
			if 'video_link' in request.POST:	# Si existe video_link, deja vacío video_file, ya que ya existe una fuente de video
				video.video_file = None
			elif 'video_file' in request.FILES:	# Si existe video_file, deja vacío video_link, ya que ya hay una fuente para el archivo 
				video.video_link = None
			video.save()	# Se guarda video
			return redirect('/myapp/success.html')
	else:
		form = VideoForm()
	return render(request, 'myapp/create_video.html',{'form':form})
