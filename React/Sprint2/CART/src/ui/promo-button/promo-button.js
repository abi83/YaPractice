import React from 'react';
import styles from './promo-button.module.css';
import closeIcon from '../../images/close.svg';

export const PromoButton = ({ children, setPromo, setDiscount, extraClass }) => {
  const cancelPromo = () => {
    setPromo('');
    setDiscount(null);
  };
  return (
    <button type="button" className={`${styles.button} ${extraClass}`} onClick={cancelPromo}>
      {children}
      <img className={styles.close} src={closeIcon} alt="кнопка закрытия" />
    </button>
  );
};
