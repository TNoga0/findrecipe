import Tagify from "@yaireo/tagify";
import React, {useState} from "react";
import Tags from "@yaireo/tagify/dist/react.tagify";
import "../App.css";

function TagField({ initialValue = [], suggestions = [], contentsCallback}) {

  const baseTagifySettings = {
    blacklist: [],
    backspace: "edit",
    placeholder: "Enter ingredients...",
    editTags: 1,
    dropdown: {
      enabled: 1,
      maxItems: 5,
    },
    callbacks: {},
    duplicates: false
  };


  const handleChange = (e) => {
    contentsCallback(e.detail.tagify.value.map(item => item.value));
  };


  const settings = {
    ...baseTagifySettings,
    whitelist: suggestions,
    callbacks: {
      add: handleChange,
      remove: handleChange,
      blur: handleChange,
      edit: handleChange,
      click: handleChange,
      "edit:updated": handleChange,
      "edit:start": handleChange
    }
  };

  return (
    <div className="TagField">
      <div className="form-group">
        <Tags settings={settings} initialValue={initialValue} />
      </div>
    </div>
  );
}

export default TagField;
