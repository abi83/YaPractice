import React, { useContext } from 'react';
import styles from './promo-button.module.css';
import closeIcon from '../../images/close.svg';

import { DiscountContext } from '../../services/appContext';
import { PromoContext } from '../../services/productsContext';

export const PromoButton = ({ children, extraClass }) => {
  const { setPromo } = useContext(PromoContext);
  const { setDiscount } = useContext(DiscountContext);

  const cancelPromo = () => {
    setPromo('');
    setDiscount(0);
  };

  return (
    <button type="button" className={`${styles.button} ${extraClass}`} onClick={cancelPromo}>
      {children}
      <img className={styles.close} src={closeIcon} alt="кнопка закрытия" />
    </button>
  );
};
