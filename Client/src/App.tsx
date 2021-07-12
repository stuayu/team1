import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import ProductPage from "./components/pages/ProductPage";
import LoginPage from "./components/pages/LoginPage";
import TablePage from "./components/pages/TablePage";
import TablePage2 from "./components/pages/TablePage2";
//import HomePage from "./components/pages/HomePage";
//<Route path="/" component={HomePage} exact />
const App: React.FC = () => {
  return (
    <Router>
      <Switch>
        <Route path="/products" component={ProductPage} exact />
        
        <Route path="/login" component={LoginPage} exact />

        <Route path="/Table" component={TablePage} exact />

        <Route path="/Table2" component={TablePage2} exact />
      </Switch>
    </Router>
  );
};

export default App;