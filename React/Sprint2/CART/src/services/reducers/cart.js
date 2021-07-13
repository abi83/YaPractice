import {INCREASE_ITEM, CANCEL_PROMO, DECREASE_ITEM, DELETE_ITEM, TAB_SWITCH} from '../actions/cart'
import { items, recommendedItems } from '../initialData'


const initialState = {
  items: items,
  recommendedItems: items,

  promoCode: '',
  promoDiscount: null,

  currentTab: 'items'
};


export const cartReducer = (state = initialState, action) => {
  switch (action.type) {
    case INCREASE_ITEM: return state
    case CANCEL_PROMO: return state
    case DECREASE_ITEM: return state
    case DELETE_ITEM: return state
    case TAB_SWITCH: return state
    default: return state
  }
}