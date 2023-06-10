import openai as op
import gradio as gr

## Need to create your own api key
op.api_key = "api_key"

## The ImageGenerator Function
def ImageGenerator(Title,Number_Of_Images,Size_Of_Image):
    response = op.Image.create(prompt = Title,
    n = int(Number_Of_Images),
    size = Size_Of_Image ) ## size of 256x256, 512x512, or 1024x1024
    image_url = response['data'][0]['url']
    return image_url




### The Text-to-Image application
def app():

    app = gr.Interface(fn=ImageGenerator, inputs = ["text","text","text"], outputs = "image", title = "Text-to-Image application",)
    return app.launch(share=True)


app()