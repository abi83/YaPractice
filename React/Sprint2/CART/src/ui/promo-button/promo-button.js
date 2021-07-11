import React from 'react';
import styles from './promo-button.module.css';
import closeIcon from '../../images/close.svg';
import {
  PromoContext,
  DiscountContext,
} from '../../services/appContext';


export const PromoButton = ({ children, extraClass }) => {
  const { setPromo } = React.useContext(PromoContext);
  const { setDiscount } = React.useContext(DiscountContext);

  
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
