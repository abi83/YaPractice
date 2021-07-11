import React from 'react';
import styles from './app.module.css';
import { Title } from '../../ui/title/title';
import { Cart } from '../cart';
import { TotalPrice } from '../common/total-price';
import {TotalPriceContext, DiscountContext} from '../../services/appContext'


function App() {
  const [totalPrice, setTotalPrice] = React.useState(0);
  const [discount, setDiscount] = React.useState(null);

  return (
    <div className={styles.app}>
      <TotalPriceContext.Provider value={{totalPrice, setTotalPrice}}>
        <DiscountContext.Provider value={{discount, setDiscount}}>
          <Title text={'Корзина'} />
          <Cart
            // setTotalPrice={setTotalPrice}
            // totalPrice={totalPrice}
            // setDiscount={setDiscount}
            // discount={discount}
          />
          <TotalPrice
              // totalPrice={totalPrice} discount={discount}
          />
        </DiscountContext.Provider>
      </TotalPriceContext.Provider>
    </div>
  );
}

export default App;
