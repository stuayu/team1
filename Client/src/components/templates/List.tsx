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

const DATA = 'http://localhost:4000/getSub/';
const LINK = 'http://localhost:3000/';
// トークンをローカルストレージから取得する
var param = new URLSearchParams();
const token = localStorage.getItem('token')?.toString();
if (token != null) {
  param.append('token', token);
}
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
      const res = await axios.post(DATA, param);
      setId(res.data.id)
      setSub_name(res.data.sub_name)
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
    window.location.href = "http://localhost:3000/attend?id=" + id ; // 通常の遷移 
  }
  return (
    <Grid container>
      <Stack spacing={2} direction="row">
        <Button variant="contained" href={LINK} >ログインページに戻る</Button>
      </Stack>
      <TableContainer component={Paper}>
        <Table sx={{ minWidth: 650 }} aria-label="simple table">
          <TableHead>
            <TableRow style={{ backgroundColor: "#F2F2F2" }}>
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
    </Grid>
  );
}
