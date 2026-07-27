import { useState } from "react";
import api from "../api";

<div style={{
display:"flex",
gap:"10px",
marginBottom:"20px",
flexWrap:"wrap"
}}>

<button>📈 Pipeline</button>

<button>💰 Revenue</button>

<button>📊 Leadership</button>

<button>⚠ Risks</button>

</div>

export default function ChatBox() {

    const [question, setQuestion] = useState("");
    const [messages, setMessages] = useState([]);
    const [loading, setLoading] = useState(false);

    async function askQuestion() {

        if (!question.trim()) return;

        const userMessage = {
            role: "user",
            text: question
        };

        setMessages(prev => [...prev, userMessage]);

        setLoading(true);

        try {

            const res = await api.post("/chat", {
                question
            });

            const aiMessage = {
                role: "assistant",
                text: res.data.answer
            };

            setMessages(prev => [...prev, aiMessage]);

        } catch (err) {

            setMessages(prev => [...prev,{
                role:"assistant",
                text:"❌ Failed to connect to backend."
            }]);

        }

        setLoading(false);
        setQuestion("");

    }

    return (

        <div style={{
            background:"white",
            padding:"20px",
            borderRadius:"10px",
            boxShadow:"0 2px 10px rgba(0,0,0,.1)"
        }}>

            <h2>AI Business Assistant</h2>

            <div style={{
                height:"350px",
                overflowY:"auto",
                border:"1px solid #ddd",
                padding:"15px",
                marginBottom:"20px"
            }}>

                {messages.map((m,index)=>(

                    <div
                        key={index}
                        style={{
                            textAlign:m.role==="user"?"right":"left",
                            marginBottom:"15px"
                        }}
                    >

                        <div
                            style={{
                                display:"inline-block",
                                background:m.role==="user"?"#2d6cdf":"#ececec",
                                color:m.role==="user"?"white":"black",
                                padding:"12px",
                                borderRadius:"12px",
                                maxWidth:"70%"
                            }}
                        >
                            {m.text}
                        </div>

                    </div>

                ))}

                {loading && <p>🤖 Thinking...</p>}

            </div>

            <input

                style={{
                    width:"80%",
                    padding:"12px",
                    marginRight:"10px"
                }}

                value={question}

                placeholder="Ask anything..."

                onChange={(e)=>setQuestion(e.target.value)}

                onKeyDown={(e)=>{

                    if(e.key==="Enter")
                        askQuestion()

                }}

            />

            <button
                onClick={askQuestion}
                style={{
                    padding:"12px 20px",
                    cursor:"pointer"
                }}
            >

                Send

            </button>

        </div>

    );

}