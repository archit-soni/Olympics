import React, { useState } from "react";

const Accordion = ({ title, content, image, image2 }) => {
  const [isActive, setIsActive] = useState(false);

  return (
    <div className="accordion-item">
      <div className="accordion-title" onClick={() => setIsActive(!isActive)}>
        <div>{title}</div>
        <div>{isActive ? "-" : "+"}</div>
      </div>
      {isActive && (
        <div className="accordion-content">
          <a href={content}> Link for raw predicted csv file</a>
          <div className="accordion-image">
            <img className="accordion-image" src={image} />
          </div>
          <div className="accordion-image">
            <img className="accordion-image" src={image2} />
          </div>
        </div>
      )}
    </div>
  );
};

export default Accordion;
