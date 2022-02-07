import plotly.express as px

def heatmap(distancematrix):
    return px.imshow(distancematrix,title="Jaccard index between lyric lines")
