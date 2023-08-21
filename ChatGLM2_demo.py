from modelscope.utils.constant import Tasks
from modelscope import Model
from modelscope.pipelines import pipeline
import gradio as gr

model = Model.from_pretrained('ZhipuAI/chatglm2-6b', device_map='auto', revision='v1.0.7')
pipe = pipeline(task=Tasks.chat, model=model)

def answer(question):
    questions = {'text':question, 'history': []}
    result = pipe(questions)
    return result.response

iface = gr.Interface(fn=answer,
                     inputs=gr.inputs.Textbox(lines=7, label="输入问题"),
                     outputs="text",
                     title="ChatGLM2-6B-FastWeb")

if __name__ == "__main__":
    iface.launch(share=False)
    #iface.launch(share=True)