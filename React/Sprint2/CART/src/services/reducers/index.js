import { combineReducers } from 'redux';
import { cartReducer } from './cart';

import { NEXT_STEP, PREVIOUS_STEP } from '../actions';


const stepReducer = (state = 'cart', action) => {
  switch (action.type) {
    // Раскомментируйте код ниже и опишите шаг PREV_STEP
    case NEXT_STEP: {
      return state === 'cart'
        ? 'delivery'
        : state === 'delivery'
        ? 'checkout'
        : state === 'checkout'
        ? 'checkout'
        : 'checkout';
    }
    case PREVIOUS_STEP: {
      return state === 'checkout'
        ? 'delivery'
        : state === 'delivery'
        ? 'cart'
        : state === 'cart'
        ? 'cart'
        : 'cart';}
    default: {
      return state;
    }
  }
};

export const rootReducer = combineReducers({
  cart: cartReducer,
  step: stepReducer
});
