import React from "react";

export default function DropTarget(props) {
  const { puzzleElement } = props;
  return (
    <li
      className="listItem"
      onDragOver={(e)=>e.preventDefault()}
    >
      {puzzleElement.elementSrc && (
        <img
          src={`./${puzzleElement.elementSrc}`}
        />
      )}
    </li>
  );
}
