import React, { useMemo } from 'react';
import styles from './postponed-container.module.css';
import { useSelector } from 'react-redux';
import { Postponed } from './postponed';

export const PostponedContainer = () => {
  const { postponed } = useSelector(state => state.cart);

  const content = useMemo(
    () => {
      return postponed.map((item, index) => {
        return <Postponed key={index} {...item} />;
      });
    },
    [postponed]
  );

  return (
    <div className={styles.container}>
      {content}
      {!postponed.length && (
        <div className={styles.postponed}>
          <p className={styles.postponedMessageText}>Здесь пусто.</p>
          <p className={styles.postponedMessageText}>
            Вы можете добавить товары в список отложенных, перетащив их карточку из корзины сюда.
          </p>
          <p className={styles.postponedMessageText}>
            Положить их обратно в корзину можно аналогичным способом.
          </p>
        </div>
      )}
    </div>
  );
};
