import React from "react";
import '../App.css';
import {
  BrowserRouter as Router,
  Link,
  Switch,
  Route,
} from "react-router-dom"
import About from "./About";
import Instructions from "./Instructions";
import ContentsForm from "./ContentsForm";
import Results from "./Results";

function Menu() {
  return (
    <Router>

      <div className="Menu">
        <div className="container-nav">
          <nav className="navbar navbar-inverse">
            <div className="navbar-header">
              <span className="navbar-brand">Recipe Finder</span>
            </div>
            <ul className="navbar-nav flex-row ml-auto">
              <li><Link to="/">Home</Link></li>
              <li><Link to="/about">About/Contact</Link></li>
            </ul>
          </nav>
        </div>
      </div>

      <Switch>
        <Route path="/about" component={About}/>
      </Switch>
      <Switch>
        <Route path="/results" component={Results}/>
      </Switch>
      <Switch>
        <Route exact path="/">
          <Instructions />
          <ContentsForm />
        </Route>
      </Switch>

    </Router>
  );
}

export default Menu;

