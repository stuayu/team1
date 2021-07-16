import * as React from 'react';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import axios from 'axios';

let res
  postdata()
  async function postdata() {
    var param = new URLSearchParams();
    const token = localStorage.getItem('token')?.toString()
    if (token != null) {
      param.append('token', token)
    }
    try {
      res = await axios.post('http://localhost:8000/getSub/', param)
      console.log(res)
      await createTable()
    } catch(err){
      res = err.response
    }
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

  function createTable() {
    for (let i = 0; i < res.data.id.length; i += 1) {
    rows.push(createData( res.data.id[i], res.data.sub_name[i]));
    }
  }

export default function BasicTable() {
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
