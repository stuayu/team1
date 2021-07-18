import * as React from 'react';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import axios from 'axios';

// 解説(https://qiita.com/akinov/items/26a7fc36d7c0045dd2db)
console.log(window.location.search.slice(1))


const DATA = 'http://localhost:8000/attend/'
// トークンをローカルストレージから取得する
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
var queries=getUrlQueries()
console.log(queries['id'])
param1.append('subject_id', queries['id'])

interface Data {
  student_id: string,
  name: string,
  attend: string,
  num: number,
}

function createData(
  student_id: string,
  name: string,
  attend: string,
  num: number,
): Data {
  return { student_id, name, attend, num };
}

const rows: Data[] = [];

export default function BasicTable() {
  
  const [student_id, setId] = React.useState([]);
  const [name, setSub_name] = React.useState([]);
  const [num, setSub_number] = React.useState([]);
  const [attend, setAttend] = React.useState([]);

  // 参考ページ(https://qiita.com/Kouichi_Itagaki/items/c8e05f084fe88a086100)
  React.useEffect(() => {
    postdata()
  }, [])

  //非同期でサーバーからデータを取得
  const postdata = async () => {
    try {
        const res1 = await axios.post(DATA, param1);
        //console.log(res1)
        console.log(res1)
        console.log(res1.data)
        console.log(res1.data.student_id)

        setSub_name(res1.data.name)
        setSub_number(res1.data.num)
        setAttend(res1.data.attend)
        setId(res1.data.student_id)


    } catch (error) {
      console.error(error);
    }
  };

  function CreateTable() {
    console.log(student_id.length)
    rows.length = 0; //配列内をリセット(変な値が残ることを阻止する)
    for (let i = 0; i < student_id.length; i += 1) {
    rows.push(createData(student_id[i], name[i], attend[i], num[i]));
    }
  }
  CreateTable();
  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>学籍番号</TableCell>
            <TableCell>講義回数</TableCell>
            <TableCell>名前</TableCell>
            <TableCell>出席</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow
              key={row.student_id}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
              >
              <TableCell component="th" scope="row">
                {row.student_id}
              </TableCell>
              <TableCell>{row.num}</TableCell>
              <TableCell>{row.name}</TableCell>
              <TableCell>{row.attend}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}
