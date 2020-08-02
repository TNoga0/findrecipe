import React from "react";
import "../App.css";


function About() {
  return (
    <div className="div-content col-md-6">
      <h3 className="about-header">Well, hi there.</h3>
      <p className="content">
        This app was made with a simple purpose: to be useful.
      </p>
      <p className="content">
        It uses Django with Gunicorn and React.<br/> All the data is served from database, which is populated by
        scraping AllRecipes. <br/> The scraping process is obviously imperfect and some ingredients may be followed by non-typical
        words or abbreviations.
      </p>
      <p className="content">
        Feel free to visit my <a href="https://github.com/TNoga0">GitHub</a>, although
        it's not crowded with projects right now.
      </p>
    </div>
  );
}

export default About;
