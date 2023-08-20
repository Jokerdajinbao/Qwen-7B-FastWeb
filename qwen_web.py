from modelscope import AutoModelForCausalLM, AutoTokenizer
from modelscope import GenerationConfig
import gradio as gr

tokenizer = AutoTokenizer.from_pretrained("qwen/Qwen-7B-Chat", revision = 'v1.0.1',trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("qwen/Qwen-7B-Chat", revision = 'v1.0.1',device_map="auto", trust_remote_code=True,fp16 = True).eval()
model.generation_config = GenerationConfig.from_pretrained("Qwen/Qwen-7B-Chat",revision = 'v1.0.1', trust_remote_code=True) # 可指定不同的生成长度、top_p等相关超参

def answer(question):
    response, history = model.chat(tokenizer , question , history=None)
    return response

iface = gr.Interface(fn=answer,
                     inputs=gr.inputs.Textbox(lines=7, label="输入问题"),
                     outputs="text",
                     title="Qwen-7B-Chat-FastWeb")

if __name__ == "__main__":
    iface.launch(share=False)
    #iface.launch(share=True)
