import React from 'react';
import suezTrafficStyles from './suez-traffic.module.css';
import { ReactComponent as NavigationIconImage } from '../../images/arrow.svg';

const GAP = 60;
const ALLOWABLE_DIFFERENCE = 30;
const MAX_TRAFFIC_LOAD = 100;
const INITIAL_TRAFFIC_LOAD = [
  {
    color: '#BDFF00',
    value: 0
  },
  {
    color: '#FA290C',
    value: 36.46
  },
  {
    color: '#000000',
    value: 42.71
  },
  {
    color: '#FA290C',
    value: 51.04
  },
  {
    color: '#DBFF00',
    value: 74.48
  },
  {
    color: '#00E717',
    value: 100
  }
];

const getCoordinates = currentCoordinate =>
  Math.floor(
    Math.random() * (currentCoordinate + GAP - (currentCoordinate - GAP)) +
      (currentCoordinate + GAP)
  );
const getTrafficLoad = currentTrafficValue => {
  const newTrafficValue = Math.floor(
    Math.random() * (MAX_TRAFFIC_LOAD - currentTrafficValue) + currentTrafficValue
  );
  return newTrafficValue - currentTrafficValue > ALLOWABLE_DIFFERENCE
    ? getTrafficLoad(currentTrafficValue)
    : newTrafficValue;
};

export default function SuezTraffic() {
  const [coordinate, setCoordinate] = React.useState(0);
  const [load, setLoad] = React.useState([]);

  React.useEffect(() => {
    const interval = setInterval(() => {
      setCoordinate(getCoordinates(coordinate));
    }, 4000);

    setLoad(INITIAL_TRAFFIC_LOAD);

    return () => clearInterval(interval);
  }, []);

  const generateLoad = React.useMemo(
      () =>
        load.reduce(
          (acc, reducer, position) => [
            ...acc,
            {
              color: reducer.color,
              value: getTrafficLoad(acc[position - 1] ? acc[position - 1].value : 0)
            }
          ],
          []
        ), [load])

  const renderTrafficBar = generateLoad
    .map(element => `${element.color} ${element.value}%`)
    .join(', ');

  const trafficBarStyles = {
    background: `linear-gradient(90deg, ${renderTrafficBar})`
  };

  return (
    <div className={suezTrafficStyles.root}>
      <NavigationIconImage
        style={{ transform: `rotate(${coordinate}deg)` }}
        className={suezTrafficStyles.arrow}
      />
      <div className={suezTrafficStyles.trafficBarContainer}>
        <span className={suezTrafficStyles.trafficBar} style={trafficBarStyles} />
      </div>
    </div>
  );
}
