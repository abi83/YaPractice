const STATUS_CONFIRMED = 'confirmed';
const STATUS_PENDING = 'pending';
const STATUS_CANCELED = 'canceled';

const renderStatus = {
  confirmed: 'Подтверждён',
  pending: 'Не подтверждён',
  canceled: 'Отменён'
};

class User extends React.Component {
  render() {
    return (
      <div className="user">
        <img className="user__avatar" src={this.props.avatar} alt="фото." />
        <div className="user__info">
          <p className="user__text">{`${this.props.name}, ${this.props.role}`}</p>
          {this.props.status && (
            <p className={`user__status ${this.props.status}`}>{renderStatus[this.props.status]}</p>
          )}
        </div>
      </div>
    );
  }
}

class CalendarEvent extends React.Component {
  state = {
    currentUser: 34047044,
    owner: { id: 34049221, name: 'Павел', role: 'Технический директор', avatar: './images/1.png' },
    subject: 'Обсуждение редизайна административной панели сайта',
    invited: [
      {
        id: 34049119,
        name: 'Татьяна',
        role: 'Дизайнер',
        status: STATUS_CONFIRMED,
        avatar: './images/2.png'
      },
      {
        id: 34047044,
        name: 'Кирилл',
        role: 'Разработчик',
        status: STATUS_PENDING,
        avatar: './images/3.png'
      },
      {
        id: 34048196,
        name: 'Константин',
        role: 'Менеджер',
        status: STATUS_CANCELED,
        avatar: './images/4.png'
      }
    ],
    durationdate: '10.11.2021',
    timeStart: '14:30',
    duration: 40,
    location: 'Переговорная №4'
  };

  getCurrentUserConfirmationStatus() {
    return this.state.invited
      .find((user)=>{
        return user.id===this.state.currentUser
      })
      .status
  }

  confirm() {
    let invited = this.state.invited;
    invited
    .find(user=>user.id === this.state.currentUser)
        .status = STATUS_CONFIRMED
    this.setState({
      ...this.state,
      invited: invited
    })
  }

  cancel() {
    let invited = this.state.invited;
    invited
    .find(user=>user.id === this.state.currentUser)
        .status = STATUS_CANCELED
    this.setState({
      ...this.state,
      invited: invited
    })
  }

  render() {
    const confirmed = this.getCurrentUserConfirmationStatus() === STATUS_CONFIRMED;
    return (
      <section className="main">
        <div className="calendar">
          <p className="calendar__menu">Тема:</p>
          <h1 className="calendar__title">{this.state.subject}</h1>
          <p className="calendar__menu">Организатор:</p>
          <User {...this.state.owner} />
          <p className="calendar__menu">Приглашены:</p>
          <div className="calendar__invited">
            {this.state.invited.map((user, index) => (
              <User key={index} {...user} />
            ))}
          </div>
          <p className="calendar__menu">Дата:</p>
          <p className="calendar__text">{this.state.durationdate}</p>
          <p className="calendar__menu">Начало:</p>
          <p className="calendar__text">{this.state.timeStart}</p>
          <p className="calendar__menu">Продолжительность:</p>
          <p className="calendar__text">{this.state.duration}</p>
          <p className="calendar__menu">Место:</p>
          <p className="calendar__text">{this.state.location}</p>
        </div>
        <div className="buttons">
          <button className="button cancel" type="button" onClick={this.cancel.bind(this)}>
            Отменить
          </button>
          <button className="button confirm" type="button" onClick={this.confirm.bind(this)}>
            Подтвердить
          </button>
        </div>
      </section>
    );
  }
}

ReactDOM.render(<CalendarEvent />, document.querySelector('#root'));
