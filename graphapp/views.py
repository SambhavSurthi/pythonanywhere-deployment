import matplotlib.pyplot as plt
from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from .forms import DataForm

def plot_graph(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            # Extracting data from the form
            x_values = [float(i) for i in form.cleaned_data['x_values'].split(',')]
            y_values = [float(i) for i in form.cleaned_data['y_values'].split(',')]

            # Generate the graph
            fig, ax = plt.subplots()
            ax.plot(x_values, y_values)
            ax.set_title('User Generated Graph')
            ax.set_xlabel('X-axis')
            ax.set_ylabel('Y-axis')

            # Save the figure to a bytes buffer
            buffer = BytesIO()
            canvas = FigureCanvas(fig)
            canvas.print_png(buffer)
            plt.close(fig)

            # Return the image as an HttpResponse
            return HttpResponse(buffer.getvalue(), content_type='image/png')

    else:
        form = DataForm()

    return render(request, 'index.html', {'form': form})
