import matplotlib.pyplot as plt
import base64
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x):
    plt.switch_backend('AGG')
    plt.figure(figsize=(4, 4))
    plt.imshow(x)
    plt.axis('off')
    plt.tight_layout(pad=0.0, w_pad=0.0, h_pad=0.0)
    graph = get_graph()
    return graph
    