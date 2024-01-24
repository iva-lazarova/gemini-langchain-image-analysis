import os
import PIL
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI


api_key = os.getenv("GOOGLE_API_KEY")
llm = ChatGoogleGenerativeAI(model="gemini-pro-vision")

message = HumanMessage(
    content=[
        {"type": "text",
         "text": "Find the differences between the two images. \n"
                 "Use as many words as you need." 'n'
                 "Provide a summary and main differences listed in bullets"
        },
        {"type": "image_url",
         "image_url": "https://fastly.picsum.photos/id/75/1999/2998.jpg?hmac=0agRZd8c5CRiFvADOWJqfTv6lqYBty3Kw-9LEtLp_98"
        },
        {"type": "image_url",
         "image_url": "https://fastly.picsum.photos/id/82/1500/997.jpg?hmac=VcdCqu9YiLpbCtr8YowUCSUD3-245TGekiXmtiMXotw"}
    ]
)

response = llm.invoke([message])
print(response.content)