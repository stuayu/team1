import React, { Component } from 'react';
import axios from "axios";
import MaterialTable from 'material-table';
 
class Getpcinfo extends Component {
    constructor(props) {
    super(props);
    this.state = {
      info: [],
      isLoading: true
    };
    this.getData = this.getData.bind(this);
  }
 
  getData() {
    axios
      .get('http://127.0.0.1:8000/db/',{
        headers: {
          accept: 'application/json'
        }
      })
      .then(results => {
        const data = results.data.content;        
        this.setState({
          info: data,
          isLoading: false
        });
      });
    }
}
return (
<div>                           
  <MaterialTable
  title="PC INFO"
  columns={columns}
  data={this.state.info}
  options={{
    pageSize: 10,
    pageSizeOptions: [10, 20,50, 100, 200, 300, 400 ,500],
    toolbar: true,
    paging: true
  }}
  />        
  <Button variant="contained" color="primary" onClick={this.getData}>info get</Button>
  </div>
)

  export default Getpcinfo