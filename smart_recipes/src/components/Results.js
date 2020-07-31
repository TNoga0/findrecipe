import React, {useState} from "react";
import { Card } from 'react-bootstrap';
import { Row, Col } from 'react-simple-flex-grid';
import "react-simple-flex-grid/lib/main.css";

const Results = props => {

  const {recipe_data} = (props.location && props.location.state) || {};

  if(recipe_data.length == 0){
    return(
      <div className="div-content col-md-6">
        <h3 className="about-header">Unfortunately, no recipe matching your fridge contents was found :(</h3>
        <h3 className="about-header">Use "Home" to return to homepage and try again!</h3>
      </div>
    );
  }
  else {
    let recipes = JSON.parse(recipe_data);

    return (
      <div className="Results">
          <Row justify="center">
            {recipes.map((recipe, index) => (
              <Col xs={{ span: 12 }} sm={{ span: 6 }} md={{ span: 6 }}
                   lg={{ span: 4 }} xl={{ span: 3 }}>
                  <Card style={{ width: '15em' }}>
                    <Card.Img className="text-center" variant='top' src={recipe.fields.image_url} />
                    <Card.Body>
                      <Card.Title className="text-center">{recipe.fields.name}</Card.Title>
                      <Card.Text></Card.Text>
                      <div className="text-center">
                        <a href={recipe.fields.address} className="btn btn-primary btn-card">Go to recipe</a>
                      </div>
                    </Card.Body>
                  </Card>
              </Col>
            ))}

          </Row>
          <br/><br/><br/>
        </div>
    );
  }

};

export default Results;
