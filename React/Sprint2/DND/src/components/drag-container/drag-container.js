import React, { useEffect, useState } from "react";
import DragList from "../drag-list/drag-list";
import DropTarget from "../drop-target/drop-target";
import puzzleImage from "../../images/puzzle.png";

export default function DragContainer() {
  const [sourceElements, setSourceElements] = useState([]);
  const [draggedElements, setDraggedElements] = useState([]);
  const [draggedElement, setDraggedElement] = useState({});

  useEffect(() => {
    const parts = [...Array(25)]
      .map((element, index) => ({
        elementSrc: `puzzle-piece-${index}.png`,
        id: index
      }))
      .sort(() => Math.random() - 0.5);
    const emptyPuzzleData = [...Array(25)].map(() => ({}));

    setSourceElements([...parts]);
    setDraggedElements([...emptyPuzzleData]);
  }, []);

  const handleDrop = (e, index) => {
    e.preventDefault();
    setSourceElements([
      ...sourceElements.filter((element) => element.id !== draggedElement.id)
    ]);

    setDraggedElements(
      draggedElements.map((element, elementIndex) => {
        return elementIndex === index ? draggedElement : element;
      })
    );

    setDraggedElement({});
  };

  const handleDrag = (e, currentElement) => {
    e.preventDefault();
    setDraggedElement(currentElement);
  };

  return (
    <section className="container">
      <ul className="list">
        {sourceElements.map((item) => (
          <DragList key={item.id} puzzleElement={item} handleDrag={handleDrag} />
        ))}
      </ul>

      <ul className="list" style={{ backgroundImage: `url(${puzzleImage})` }}>
        {draggedElements.map((item, index) => (
          <DropTarget
            key={index}
            dropTargetIndex={index}
            puzzleElement={item}
            handleDrop={handleDrop}
          />
        ))}
      </ul>
    </section>
  );
}
