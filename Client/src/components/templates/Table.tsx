import * as React from 'react';
import { DataGrid, GridColDef, GridValueGetterParams } from '@material-ui/data-grid';
import get from "Axios/PersonList-get";

const columns: GridColDef[] = [
  { field: 'id', headerName: '学籍番号', width: 200 },
  { field: 'fullName', headerName: '氏名', width: 200 },
  {
    field: 'idm',headerName: 'IDm',width: 200},
  { field: 'Attend', headerName: '出席状況',width:200},
];

const rows = [ //ここはデータベースから出席状況や履修登録情報をもらう
  { id: 'B21P034', fullName: 'Snow', idm: '????', Attend: '出席' },
  { id: 'B21P035', fullName: 'Lannister', idm: 'Cersei', Attend: '欠席' },
  { id: 'B21P036', fullName: 'Lannister', idm: 'Jaime', Attend: '遅刻' },
  { id: 'B21P037', fullName: 'Stark', idm: 'Arya', Attend: '遅刻' },
  { id: 'B21P038', fullName: 'Targaryen', idm: 'Daenerys', Attend: '遅刻' },
  { id: 'B21P039', fullName: 'Melisandre', idm: null, Attend: '遅刻' },
  { id: 'B21P040', fullName: 'Clifford', idm: 'Ferrara', Attend: '遅刻' },
  { id: 'B21P041', fullName: 'Frances', idm: 'Rossini',Attend: '遅刻' },
  { id: 'B21P042', fullName: 'Roxie', idm: 'Harvey', Attend: '遅刻'},
];

export default function DataTable() {
  return (
    <div style={{ height: 400, width: '100%' }}>
      <DataGrid rows={rows} columns={columns} pageSize={100} checkboxSelection />
    </div>
  );
}
