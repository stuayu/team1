import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import ProductPage from "./components/pages/ProductPage";
import LoginPage from "./components/pages/LoginPage";
import HomePage from "./components/pages/HomePage";

const App: React.FC = () => {
  return (
    <Router>
      <Switch>
        <Route path="/products" component={ProductPage} exact />
        <Route path="/" component={HomePage} exact />
        <Route path="/login" component={LoginPage} exact />
      </Switch>
    </Router>
  );
};

export default App;