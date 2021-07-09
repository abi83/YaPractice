import React from 'react';
import styles from './app.module.css';
import { Title } from '../../ui/title/title';
import { Cart } from '../cart';
import { TotalPrice } from '../common/total-price';

function App() {
  const [totalPrice, setTotalPrice] = React.useState(0);
  const [discount, setDiscount] = React.useState(null);
  
  return (
    <div className={styles.app}>
      <Title text={'Корзина'} />
      <Cart totalPrice={totalPrice} discount={discount} setTotalPrice={setTotalPrice} setDiscount={setDiscount}/>
      <TotalPrice totalPrice={totalPrice} discount={discount}/>
    </div>
  );
}

export default App;
