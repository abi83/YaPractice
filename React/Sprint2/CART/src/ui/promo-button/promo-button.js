import React, { useContext } from 'react';
import styles from './promo-button.module.css';
import closeIcon from '../../images/close.svg';

import { DiscountContext } from '../../services/appContext';
import { PromoContext } from '../../services/productsContext';

export const PromoButton = ({ children, extraClass }) => {
  const { setPromo } = useContext(PromoContext);
  const { discountDispatcher } = useContext(DiscountContext);

  const cancelPromo = () => {
    setPromo('');
    discountDispatcher({type: 'reset'});
  };

  return (
    <button type="button" className={`${styles.button} ${extraClass}`} onClick={cancelPromo}>
      {children}
      <img className={styles.close} src={closeIcon} alt="кнопка закрытия" />
    </button>
  );
};
