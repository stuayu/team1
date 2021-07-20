import * as React from 'react';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import axios from 'axios';
import { Grid } from '@material-ui/core';
import Stack from '@material-ui/core/Stack';
import Button from '@material-ui/core/Button';
import { ConstructionRounded } from '@material-ui/icons';
//import Graph from "./graph";

// 解説(https://qiita.com/akinov/items/26a7fc36d7c0045dd2db)
console.log(window.location.search.slice(1))
var queries=getUrlQueries()
const LINK = 'http://localhost:3000/graph?id=' + queries['id'];
const DL_LINK = 'http://localhost:8000/csv/';
var param2 = new URLSearchParams();
const DATA = 'http://localhost:8000/attend/';
// トークンをローカルストレージから取得する
var param1 = new URLSearchParams();
const token = localStorage.getItem('token')?.toString()
if (token != null) {
  param1.append('token', token);
  param2.append('token', token);
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

console.log(queries['id'])
param1.append('subject_id', queries['id'])
param2.append('id', queries['id']);
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
  /*
  function downloadCSV() {
    //ダウンロードするCSVファイル名を指定する
    const filename = "attend.csv";
    //CSVデータ
    //const data = "テスト, テスト, テスト\nテスト, テスト, テスト";
    //BOMを付与する（Excelでの文字化け対策）
    const bom = new Uint8Array([0xef, 0xbb, 0xbf]);
    //Blobでデータを作成する
    const blob = new Blob([bom, rows.map()], { type: "text/csv" });

    //IE10/11用(download属性が機能しないためmsSaveBlobを使用）
    if (window.navigator.msSaveBlob) {
        window.navigator.msSaveBlob(blob, filename);
    //その他ブラウザ
    } else {
        //BlobからオブジェクトURLを作成する
        const url = (window.URL || window.webkitURL).createObjectURL(blob);
        //ダウンロード用にリンクを作成する
        const download = document.createElement("a");
        //リンク先に上記で生成したURLを指定する
        download.href = url;
        //download属性にファイル名を指定する
        download.download = filename;
        //作成したリンクをクリックしてダウンロードを実行する
        download.click();
        //createObjectURLで作成したオブジェクトURLを開放する
        (window.URL || window.webkitURL).revokeObjectURL(url);
    }
}*/

  let datapost:string = '';
  console.log(param2);
  console.log(param1);

  function handleClick(){
    axios.post(DL_LINK,param2)
    .then(result=>downloadCSV(result.data, 'text/csv', 'test.csv'))
    .catch((error) => {
      if (error.response) {
        // 200系以外の時にエラーが発生する
        console.log(error.response.data);
        console.log(error.response.status);
        console.log(error.response.headers);
      } else if (error.request) {
        console.log(error.request);
      } else {
        // 上記以外のエラーが発生した場合
        console.log('Error', error.message);
      }
    });
    console.log(datapost);
  }


  /*let data_DL:string = '';
  function handleClick(event) {
    React.useEffect(() => {
      datapost()
    }, [])
    const datapost = async () => {
      try {
        data_DL = await axios.post(DL_LINK, param2);
       
     } catch (error) {
       console.error(error);
     }
    }
  }*/

  function downloadCSV(textdata, filetype, filename) {
    let data = textdata.map((record)=>record.join(',')).join('\r\n');
    let bom  = new Uint8Array([0xEF, 0xBB, 0xBF]);
    const blob = new Blob([bom,data], {type: filetype});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    a.click();
    URL.revokeObjectURL(url);
  }


  CreateTable();
  return (
    <Grid container >
      <Stack spacing={2} direction="row">
        <Button variant="contained" href={LINK} >グラフ表示</Button>
        <Button variant="contained" onClick={event => handleClick()} >出席状況ダウンロード</Button>
      </Stack>
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow style={{ backgroundColor: "#F2F2F2" }}>
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
    
    </Grid>
  );
}
