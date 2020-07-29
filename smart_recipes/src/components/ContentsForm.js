import React, { useState, useEffect } from "react";
import TagField from "./TagField";
import "../App.css";
import '@yaireo/tagify/dist/tagify.css';
import $ from 'jquery';
import recipes from "../apis/recipes";
import DjangoCSRFToken from "django-react-csrftoken/src";
import { Redirect } from 'react-router-dom';


const ContentsForm = (props) => {

  const [contents, setContents] = useState("");
  const [meal_type, setMealType] = useState("");

  //PROP TO PUSH AFTER RECEIVING RESPONSE
  const [processed_recipes, setProcessedRecipes] = useState([]);
  const [redirect, setRedirect] = useState(false);

  //API
  const [ingredientdata, setIngredientData] = useState([]);

  useEffect(() => {
    const fetchRecipes = async () => {
      await recipes.get('/ingredients/')
        .then(
          resp => {
            setIngredientData(resp.data);
          }
        );
    };
    fetchRecipes();
  }, []);
  //END API

  //CRF TOKEN AND FORM SUBMIT

  let $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');

  const handleSubmit = (event) => {
    event.preventDefault();
    fetch("/process/", {
      method: "POST",
      cache: "no-cache",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": $crf_token
      },
      body: JSON.stringify({contents: contents, meal_type: meal_type})
    })
      .then(response => response.json())
    // RESPONSE:
    .then(recipes => {
      setProcessedRecipes(recipes);
      setRedirect(true);
    });
  };
  //END CRF TOKEN AND FORM SUBMITr

  //RENDERING
  if(ingredientdata.length == 0) {
    return (
      <div className="ContentsForm">
        <div className="div-content col-md-6">
          <h3>Loading data...</h3>
        </div>
      </div>
    )
  }
  else if (redirect == true){
    return(
      <Redirect to={{
        pathname: "/results",
        state: { recipe_data: processed_recipes }
      }} />
    );
  }
  else {
    const suggestions = Array.from(ingredientdata, x=>x.name);
    return (
      <div className="ContentsForm">
        <div className="div-content col-md-6">
          <form onSubmit={handleSubmit}>
            <DjangoCSRFToken />
            <div className="form-group">
              <label htmlFor="mealTypeInput">Select meal type</label>
              <select className="form-control"
                      id="mealTypeInput"
                      onChange={(evt) => setMealType(evt.target.value)}
              >
                <option value="breakfast">Breakfast</option>
                <option value="main_course">Main Course</option>
                <option value="dessert">Dessert</option>
                <option value="healthy">Healthy Foods</option>
              </select>
            </div>
            <div className="form-group">
              <label htmlFor="contentsInput">Input fridge/shelf contents</label>
              <div className="contentsInput">
                <TagField initialValue={[]} suggestions={suggestions} contentsCallback={setContents}/>
              </div>
            </div>
            <button type="submit" className="btn btn-primary btn-submit">Submit</button>
          </form>
        </div>
      </div>
    );
  }
}

export default ContentsForm;
