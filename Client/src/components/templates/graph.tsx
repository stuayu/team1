import React from "react"
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import axios from 'axios';

const DATA = 'http://localhost:8000/attend/'
//const data = 


var param1 = new URLSearchParams();
const token = localStorage.getItem('token')?.toString()
if (token != null) {
  param1.append('token', token)
}
param1.append('subject_id','F1')


export default function Graph() {
  const [student_id, setId] = React.useState([]);
  const [name, setSub_name] = React.useState([]);
  const [num, setSub_number] = React.useState([]);
  const [attend, setAttend] = React.useState([]);
  
  React.useEffect(() => {
    postdata()
  }, [])

  const postdata = async () => {
    try {
        const res1 = await axios.post(DATA, param1);
        setSub_name(res1.data.name)
        setSub_number(res1.data.num)
        setAttend(res1.data.attend)
        setId(res1.data.student_id)
    } catch (error) {
      console.error(error);
    }
  };

  let nnnka: number = 0;
  let nanka2: number = 0;
  let num_tmp: number = 0;
  for(let id of student_id){
    console.log(id);
    let iD = [];

    let index:number = student_id.indexOf(id);
    console.log(index);
    console.log(nanka2);
    console.log(attend[index]);

    if(index < 0) continue;

    switch(attend[num_tmp]){
      case '出席': nnnka++; break;
      case '遅刻': nanka2++; break;
    }
    num_tmp += 1; 
  }

  
  const data = [
    {
      name : 'S001',
      att : nnnka,
      seq : nanka2,
      
    }
  ]

    return (
      <BarChart
        width={500}
        height={300}
        data={data}
        margin={{
          top: 5,
          right: 30,
          left: 20,
          bottom: 5
        }}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Bar dataKey="att" fill="#8884d8" />
        <Bar dataKey="seq" fill="#82ca9d" />
      </BarChart>
    );
  }