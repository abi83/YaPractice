import { combineReducers } from 'redux';
import { cartReducer } from './cart';

const stepReducer = (state = 'cart', action) => {
  switch (action.type) {
    // Раскомментируйте код ниже и опишите шаг PREV_STEP
    // case NEXT_STEP: {
    //   return state === 'cart'
    //     ? 'delivery'
    //     : state === 'delivery'
    //     ? 'checkout'
    //     : state === 'checkout'
    //     ? 'checkout'
    //     : 'checkout';
    // }
    default: {
      return state;
    }
  }
};

export const rootReducer = combineReducers({
  cart: cartReducer,
});
