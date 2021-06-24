class Employee extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      age: 65,
      avatar: 'https://code.s3.yandex.net/react/code/albert-einstein.jpg',
      name: 'Альберт Энштейн',
      address: {
        country: 'Германия',
        city: 'Ульм'
      },
      favoriteTechnology: 'React.js'
    };
  }

  render() {
    return (
      <div className="card">
        <img className="card__image" alt="аватар" src={this.state.avatar}/>
        <h4 className="card__name">{this.state.name}</h4>
        <p className="card__text">Полных лет: {this.state.age}</p>
        <p className="card__text">Место пребывания: {this.state.address.country}, {this.state.address.city}</p>
        <p className="card__text">Любимая технология: {this.state.favoriteTechnology}</p>
      </div>
    );
  }
}

ReactDOM.render(<Employee />, document.querySelector('#root'));
