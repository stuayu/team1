import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

//import ProductPage from "./components/pages/ProductPage";
import LoginPage from "./components/pages/LoginPage";
import TablePage from "./components/templates/Axios-api2";
//import HomePage from "./components/pages/HomePage";
//<Route path="/" component={HomePage} exact />
//<Route path="/list" component={TablePage} exact />
//<Route path="/products" component={ProductPage} exact />
const App: React.FC = () => {
  return (
    <Router>
      <Switch>
        
        <Route path="/list" component={TablePage} exact />
        <Route path="/login" component={LoginPage} exact />
      </Switch>
    </Router>
  );
};

export default App;