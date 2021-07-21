import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import AttendPage from "./components/templates/attend";
import LoginPage from "./components/pages/LoginPage";
import TablePage from "./components/templates/List";
import Graph from "./components/templates/graph";

const App: React.FC = () => {
  return (
    <Router>
      <Switch>
        <Route path="/attend" component={AttendPage} exact/>
        <Route path="/list" component={TablePage} exact/>
        <Route path="/" component={LoginPage} exact />
        <Route path="/graph" component={Graph} exact />
      </Switch>
    </Router>
  );
};

export default App;