import React, { useMemo } from 'react';
import { MainButton } from '../../ui/main-button/main-button';
import styles from './total-price.module.css';
import { useDispatch, useSelector } from 'react-redux';
import { NEXT_STEP, PREVIOUS_STEP } from '../../services/actions';
import { priceFormat, totalPriceSelector } from '../common/utils';

export const TotalPrice = () => {
  const totalPrice = useSelector(totalPriceSelector);

  const discount = useSelector(state => state.cart.promoDiscount);

  const price = discount ? totalPrice - totalPrice * (discount / 100) : totalPrice;

  const step = useSelector(state => state.step);
  
  const dispatch = useDispatch();

  const prev = () => {
    dispatch({type:PREVIOUS_STEP})
  };

  const next = () => {
    dispatch({type:NEXT_STEP})
  };

  const submitButtonText = step === 'checkout' ? 'Оформить заказ' : 'Продолжить оформление';

  const buttonText = useMemo(
    () => {
      if (step === 'delivery') {
        return 'Назад к списку покупок';
      } else if (step === 'checkout') {
        return 'Назад к выбору доставки';
      } else {
        return '';
      }
    },
    [step]
  );

  const confirmOrder = () => {};

  const nextAction = step === 'delivery' || step === 'cart' ? next : confirmOrder;

  return (
    <div className={`${styles.container}`}>
      <p className={styles.text}>Итого:</p>
      <p className={styles.cost}>{priceFormat(price)}</p>
      <div className={styles.buttonbox}>
        {(step === 'delivery' || step === 'checkout') && (
          <MainButton onClick={prev} type="button" secondary={true} extraClass={styles.button}>
            {buttonText}
          </MainButton>
        )}
        <MainButton onClick={nextAction} type="button">
          {submitButtonText}
        </MainButton>
      </div>
    </div>
  );
};
