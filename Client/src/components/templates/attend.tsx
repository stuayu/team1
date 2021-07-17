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

const DATA1 = 'http://localhost:8000/number/'
const DATA2 = 'http://localhost:8000/attend/'
// トークンをローカルストレージから取得する
var param1 = new URLSearchParams();
var param2 = new URLSearchParams();
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
  id: string;
  sub_name: string;
}

function createData(
  id: string,
  sub_name: string,
): Data {
  return { id, sub_name };
}

const rows: Data[] = [];

export default function BasicTable() {
  
  const [Id, setId] = React.useState([]);
  const [Sub_name, setSub_name] = React.useState([]);

  // 参考ページ(https://qiita.com/Kouichi_Itagaki/items/c8e05f084fe88a086100)
  React.useEffect(() => {
    postdata()
  }, [])

  //非同期でサーバーからデータを取得
  const postdata = async () => {
    try {
        const res1 = await axios.post(DATA1, param1);
        const res2 = await axios.post(DATA2, param2);
        console.log(res1)
        console.log(res2)
    } catch (error) {
      console.error(error);
    }
  };

  function CreateTable() {
    rows.length = 0; //配列内をリセット(変な値が残ることを阻止する)
    for (let i = 0; i < Id.length; i += 1) {
    rows.push(createData(Id[i], Sub_name[i]));
    }
  }
  CreateTable();
  function handleClick(event,id){
    console.log(id)
    /*window.location.href = "http://localhost:3000/attend?id=" + id ; // 通常の遷移 */
    //console.log(event)
  }
  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>科目ID</TableCell>
            <TableCell>科目名</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow
              onClick={event => handleClick(event,row.id)}
              key={row.id}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell component="th" scope="row">
                {row.id}
              </TableCell>
              <TableCell>{row.sub_name}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}
