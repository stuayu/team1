import React from "react"
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend,} from 'recharts';
import axios from 'axios';
import { Grid } from "@material-ui/core";
import Stack from '@material-ui/core/Stack';
import Button from '@material-ui/core/Button';

const DATA = '/api/attend';
const LINK = '/';

var queries=getUrlQueries()

var param1 = new URLSearchParams();
const token = localStorage.getItem('token')?.toString()
if (token != null) {
  param1.append('token', token)
}
function getUrlQueries() {
    var queryStr = window.location.search.slice(1) //文頭?を削除
    var queries = {};

    // クエリがない場合は空のオブジェクトを返す
  if (!queryStr) {
    return queries;
  }

  // クエリ文字列を & で分割して処理
  queryStr.split('&').forEach(function(queryStr) {
    // = で分割してkey,valueをオブジェクトに格納
    var queryArr = queryStr.split('=');
    queries[queryArr[0]] = queryArr[1];
  });

  return queries;
}
param1.append('subject_id', queries['id'])


export default function Graph() {
  const [student_id, setId] = React.useState([]);
  const [attend, setAttend] = React.useState([]);
  
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

  let name_data: string[] = [];    //生成するデータ(学籍番号)
  let attend_data: number[] = [];  //生成するデータ(出席回数の合計値)
  let late_data: number[] = [];    //生成するデータ(遅刻回数の合計値)
  let attend_tmp: number = 0;      //出席回数を合計する際に利用する
  let late_tmp: number = 0;        //遅刻回数を合計する際に利用する
  let num_tmp: number = 0;         //forループが何回回ったのか計測する
  let index_tmp: number = 0;       //student_idから取り出した値(id)がstudent_idの何番目かを格納
  let tmp: number = 0;             //学生一人に対応できるようにするため
  let data: Object[] = [];         //生成できた結果を格納する

  const check_data = async () => {
    for(let id of student_id){
      let index: number = student_id.indexOf(id);
      if (index_tmp !== index) {
        tmp += 1;
        index_tmp = index;
        attend_tmp = 0; //変わったら変数初期化
        late_tmp = 0;   //変わったら変数初期化
      }

      if(index < 0) continue;
      switch(attend[num_tmp]){
        case '出席': attend_tmp++; break;
        case '遅刻': late_tmp++; break;
      }
      attend_data[tmp] = attend_tmp;
      late_data[tmp] = late_tmp;
      name_data[tmp] = id;
      //console.log(attend_data[tmp]);
      console.log(late_data[tmp]);
      num_tmp += 1;
    }
    await createdata();
    function createdata() {
      for (let j = 0; j <= tmp; j++){
        let demo = {
            name: name_data[j],
            att: attend_data[j],
            seq: late_data[j],
          }
        console.log(demo);
        data.push(demo);
      }
    }
  }
  

  
  check_data();

  return (
    <Grid container>
      <Stack spacing={2}>
        <Button variant="contained" href={LINK}>ログインページに戻る</Button>
      </Stack>
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
      </Grid>
    );
  }