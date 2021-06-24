class Page extends React.Component {
  render() {
    return (
      <div className={`app ${this.props.img}`}>
        <h1 className='app__greeting'>{this.props.greeting}</h1>
      </div>
    );
  }
}

class CurrentTime extends React.Component {
  render() {
    const time = new Date().getHours();
    const states = {
      morning: {greeting: 'Доброе утро', img: 'morning'},
      afternoon: {greeting: 'Добрый день', img: 'afternoon',},
      evening: {greeting: 'Добрый вечер', img: 'evening'},
      night: {greeting: 'Доброй ночи', img: 'night'},
    }
    let dayTime;
    if (time >= 4 && time <12){
      dayTime='morning'
    } else if (time >=12 && time < 16){
      dayTime='afternoon'
    } else if (time >=16 && time < 23){
      dayTime='evening'
    } else if (time < 4 || time >=23){
      dayTime='night'
    }
    return (
      <Page {...states[dayTime]} />
    )
  }
}

ReactDOM.render(<CurrentTime />, document.querySelector('#root'));