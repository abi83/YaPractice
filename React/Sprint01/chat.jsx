import React from 'react';
import './styles.css';

const Message = ({ message, repliedMessage, className = 'message' }) => (
  <div className={className}>
    {repliedMessage && <RepliedMessage message={repliedMessage} />}
    <h3>{message.user}</h3>
    <p>{message.text}</p>
  </div>
);

const RepliedMessage = ({ message }) => <Message message={message} className={'replied-message'} />;

const Chat = ({ thread }) => (
  <div className="tread">
    thread.map(
      (message, index, arr) => (
      <React.Fragment key={index}>
        <Message message={message}
          repliedMessage={arr.find((m) => m.id === message.replyTo)}
        />
      </React.Fragment>
    )
  </div>
);

export default class App extends React.Component {
  state = {
    thread: [
      {
        id: 1,
        user: 'Тамара',
        text: 'Всем привет! Кто в курсе, когда в нашем доме отключат горячую воду?'
      },
      {
        id: 2,
        user: 'Алексей',
        replyTo: 1,
        text: 'В подъезде висит объявление, скоро буду там, сфотографирую и пришлю сюда'
      },
      {
        id: 3,
        user: 'Катя',
        replyTo: 2,
        text: 'О! Спасибо! Ждём! :)'
      }
    ]
  };

  render() {
    return (
      <div className="App">
        <Chat thread={this.state.thread} />
      </div>
    );
  }
}
