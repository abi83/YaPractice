import React from 'react';
import {ReactComponent as TriangleImage} from '../../images/triangle.svg'
import coursePredictorStyles from './course-predictor.module.css';

const MIN_VALUE = 50;
const MAX_VALUE = 250;
const getRandomNum = () => (Math.random() * (MAX_VALUE - MIN_VALUE) + MIN_VALUE).toFixed(2);
const getRatio = (current, previous = 0) => ((current - previous) / (current < previous ? previous : current) * 100).toFixed(2);

export default function CoursePredictor() {
  const [currentCourse, setCurrentCourse] = React.useState();
  const previousCourseRef = React.useRef();
  
  React.useEffect(() => {
    previousCourseRef.current = currentCourse;
  });
  
  
  const previousCourse = previousCourseRef.current;

  const handleGenerateCourse = () => {
    setCurrentCourse(getRandomNum());
  };

  const isDown = getRatio(currentCourse, previousCourse) < 0 ? coursePredictorStyles.ratioDown : coursePredictorStyles.ratioUp;

  const ratioElement = (
    (currentCourse && previousCourse) &&
    <output className={isDown}>
      <TriangleImage className={coursePredictorStyles.ratioIcon} />
      {getRatio(currentCourse, previousCourse)}%
    </output>
  );

  const previousElement = (
  <p className={coursePredictorStyles.previousElement}>
    Предыдущее значение:
      {previousCourse &&
        <output className={coursePredictorStyles.value}>
          {previousCourse} ₽
        </output>
      }
  </p>
);
  

  const currentElement = (
    currentCourse &&
    <output className={coursePredictorStyles.currentElement}>
      {currentCourse} ₽
    </output>
  );

  return (
    <section className={coursePredictorStyles.card}>
      {previousElement}
      <div className={coursePredictorStyles.cardRow}>
        {currentElement}
        {ratioElement}
      </div>
      <p className={coursePredictorStyles.caption}>
        За 1 $
      </p>
      <button onClick={handleGenerateCourse} className={coursePredictorStyles.button}>
        Заглянуть в будущее
      </button>
    </section>
  )
}
