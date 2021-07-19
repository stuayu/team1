import React from "react"
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend,} from 'recharts';
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
  const [attend, setAttend] = React.useState([]);
  const [TMP, setTmp] = React.useState([]);
  
  React.useEffect(() => {
    postdata()
  }, [])

  const postdata = async () => {
    try {
        const res1 = await axios.post(DATA, param1);
        setAttend(res1.data.attend)
        setId(res1.data.student_id)
    } catch (error) {
      console.error(error);
    }
  };

  let name_data:string[] = [];
  let attend_data: number[] = [];
  let late_data: number[] = [];
  let attend_tmp: number = 0;
  let late_tmp: number = 0;
  let num_tmp: number = 0;
  let index_tmp: number = 0;
  let tmp: number = 0;

  const check_data = () => {
    for(let id of student_id){
      //console.log(id);

      let index: number = student_id.indexOf(id);
      if (index_tmp !== index) {
        tmp += 1;
        index_tmp = index;
      }
      console.log(index);
      //console.log(late_data);
      //console.log(attend[index]);

      if(index < 0) continue;
      switch(attend[num_tmp]){
        case '出席': attend_tmp++; break;
        case '遅刻': late_tmp++; break;
      }
      attend_data[tmp] = attend_tmp;
      late_data[tmp] = late_tmp;
      name_data[tmp] = id;
      //console.log(attend_tmp);
      //console.log(late_tmp);
      //console.log(id)
      //console.log(tmp);
      num_tmp += 1;
    }
    let data;
    for (let j = 0; j <= tmp; j++){
      let demo = [
        {
          name: name_data[j],
          att: attend_data[j],
          seq: late_data[j],
        }
      ];
      console.log(demo)
      data.push(demo)
    }
  }
  

  
  check_data();

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