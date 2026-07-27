import { useEffect, useState } from "react";
import api from "../api";

export default function Dashboard(){

    const [data,setData]=useState(null);

    useEffect(()=>{

        api.get("/dashboard")
        .then(res=>setData(res.data));

    },[]);

    if(!data) return <h2>Loading Dashboard...</h2>;

    return(

        <div style={{
            display:"grid",
            gridTemplateColumns:"repeat(4,1fr)",
            gap:"20px",
            marginBottom:"30px"
        }}>

            <Card
                title="💰 Revenue"
                value={`$${Math.round(data.revenue.collected_value).toLocaleString()}`}
            />

            <Card
                title="📈 Pipeline"
                value={`$${Math.round(data.pipeline.total_pipeline).toLocaleString()}`}
            />

            <Card
                title="🤝 Deals"
                value={data.pipeline.total_deals}
            />

            <Card
                title="🏗 Projects"
                value={data.active_projects}
            />

        </div>

    )

}

function Card({title,value}){

    return(

        <div style={{
            background:"white",
            borderRadius:"15px",
            padding:"25px",
            boxShadow:"0 4px 15px rgba(0,0,0,.08)"
        }}>

            <h3>{title}</h3>

            <h1>{value}</h1>

        </div>

    )

}