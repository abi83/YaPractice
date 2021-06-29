import React from 'react';
import lootboxerStyles from './lootboxer.module.css';

import lockImage from '../../images/lock.svg';
import checkImage from '../../images/check.svg';
import retryImage from '../../images/retry.svg';
import crumbsImage from '../../images/crumbs.png';
import drinkImage from '../../images/drink.png';
import monitorImage from '../../images/monitor.png';
import mouseImage from '../../images/mouse.png';
import videocardImage from '../../images/videocard.png';
import wheelImage from '../../images/wheel.png';

const itemsData = [
  {
    name: 'GeekForce RTX 9000',
    description: 'Да-да, та самая видеокарта. Теперь вам не нужно продавать почку, чтобы поиграть в самые новые игры.',
    image: videocardImage
  },
  {
    name: 'Aimbot MX420',
    description: 'Топовая игровая мышь с гиперчувствительным сенсором и эргономичным дизайном. Главное, чтобы не забанили за допинг.',
    image: mouseImage
  },
  {
    name: 'SpeedyMonster',
    description: 'Энергетический напиток, после которого можно играть в режиме нон-стоп всю неделю. Не злоупотребляйте.',
    image: drinkImage
  },
  {
    name: 'TurboRacer 001',
    description: 'С этим рулём можно входить в любой поворот и не сбавлять скорость. Забирайте, если любите запах  жжёной резины.',
    image: wheelImage
  },
  {
    name: 'Крошки из клавиатуры',
    description: 'Так бывает. Сегодня вы выигрываете, а завтра выковыриваете крошки из клавиатуры. Похоже, завтра уже наступило.',
    image: crumbsImage
  },
  {
    name: 'CrystalClearHD 27HDX',
    description: 'Ультраширокий (Очень. Широкий. Очень.) дисплей, который позволит видеть всё (кроме зарплаты к концу месяца).',
    image: monitorImage
  }
];

const getRandomElement = arr => arr[Math.floor(Math.random() * arr.length)];

class Lootboxer extends React.Component {
  state = {
    currentItem: null,
    isHovered: false
  };

  handleNewTryClick = () => {
    this.setState({
      ...this.state,
      currentItem: getRandomElement(itemsData)
    });
  };
  
  handleTakeClick = () => {
    this.setState({
      ...this.state,
      currentItem: null
    });
  }

  handleItemHover = () => {
    this.setState({
      ...this.state,
      isHovered: !this.state.isHovered
    });
  };

  render() {
    return (
      <section className={lootboxerStyles.root}>

        <p className={lootboxerStyles.description}>
          {
            this.state.currentItem && this.state.isHovered &&
            <span>{this.state.currentItem.description}</span>
          }
        </p>

        <div
          className={lootboxerStyles.card}
          onMouseEnter={this.handleItemHover}
          onMouseLeave={this.handleItemHover}
        >
          {
            !this.state.currentItem
              ? <img src={lockImage} alt='Lock' />
              : <img src={this.state.currentItem.image} alt='Item' />
          }
        </div>

        <h2
          className={lootboxerStyles.title}
          onMouseEnter={this.handleItemHover}
          onMouseLeave={this.handleItemHover}
        >
          {
            this.state.currentItem &&
            this.state.currentItem.name
          }
        </h2>

        <div className={lootboxerStyles.controls}>
          {
            !this.state.currentItem
            ? <button
                className={lootboxerStyles.button}
                onClick={this.handleNewTryClick}
              >
                Поехали
              </button>
            : <>
                <button
                  className={lootboxerStyles.button}
                  onClick={this.handleTakeClick}
                >
                  <img src={checkImage} alt='Check' />
                  Забираю
                </button>
                <button
                  className={lootboxerStyles.button}
                  onClick={this.handleNewTryClick}
                >
                  <img src={retryImage} alt='Retry' />
                  Ещё разок
                </button>
              </>
          }
        </div>
      </section>
    );
  }
}

export default Lootboxer;
