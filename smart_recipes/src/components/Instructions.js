import React from "react";
import '../App.css';

function Instructions() {
  return (
    <div className="InstructionsComponent">
      <div className="div-content col-md-6">
        <h3 className="instructions">The rules are simple:</h3>
        <div className="content">
          <ol>
            <li>you choose a desired meal type from the dropdown list</li>
            <li>in the text field you enter your fridge contents. You will receive hints from a dropdown lists - if you enter an
            ingredient that is not hinted you would not receive a recipe with said ingredient as the only ones being suggested are
            those from recipes in the database.</li>
            <li>you smash the "submit" button and wait until the app suggests some recipes</li>
          </ol>
        </div>
        <br/>
        <h3 className="instructions">Enjoy! Any feedback is appreciated.</h3>
      </div>
    </div>
  );
}

export default Instructions;
