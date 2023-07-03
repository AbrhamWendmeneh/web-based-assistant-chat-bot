import gradio
from chat_utils import CustomChatBot


demo = gradio.Interface(
    fn=CustomChatBot,
    inputs=gradio.inputs.Textbox(placeholder="Enter your query..."),
    examples=[
        ["Enabling two-factor authentication for important accounts"],
        ["Warnings about common cyber threats and scams"],
        ["Steps to remove malware and change compromised passwords"], 
        ["Recommending password managers to generate unique passwords"],
        ["How to identify phishing emails"],
        ["Recommending password managers to generate unique passwords"]  
    ],
    outputs="text",
    title="Cybersecurity Pro",
    description="Ask me anything about cybersecurity and cyber attack warnings.",
    theme="default",
    layout="horizontal",
    page_icon="🔒",
    server_name="Cybersecurity Pro",

)

demo.launch(share=True)
