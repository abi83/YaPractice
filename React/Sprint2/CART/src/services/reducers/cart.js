import {
  DELETE_ITEM,
  CANCEL_PROMO,
  DECREASE_ITEM,
  INCREASE_ITEM,
  GET_ITEMS_FAILED,
  GET_ITEMS_REQUEST,
  GET_ITEMS_SUCCESS,
  TAB_SWITCH
} from '../actions/cart';
import { recommendedItems } from '../initialData';

const initialState = {
  items: [],
  itemsRequest: false,
  itemsFailed: false,

  recommendedItems,

  promoCode: 'PROMOCODE',
  promoDiscount: 50,

  currentTab: 'items'
};

export const cartReducer = (state = initialState, action) => {
  switch (action.type) {
    case GET_ITEMS_REQUEST: {
      return {
        ...state,
        itemsRequest: true
      };
    }
    case GET_ITEMS_SUCCESS: {
      return { ...state, itemsFailed: false, items: action.items, itemsRequest: false };
    }
    case GET_ITEMS_FAILED: {
      return { ...state, itemsFailed: true, itemsRequest: false };
    }
    case TAB_SWITCH: {
      return {
        ...state,
        currentTab: state.currentTab === 'items' ? 'postponed' : 'items'
      };
    }
    case INCREASE_ITEM: {
      return {
        ...state,
        items: [...state.items].map(item =>
          item.id === action.id ? { ...item, qty: ++item.qty } : item
        )
      };
    }
    case DECREASE_ITEM: {
      return {
        ...state,
        items: [...state.items].map(item =>
          item.id === action.id ? { ...item, qty: --item.qty } : item
        )
      };
    }
    case DELETE_ITEM: {
      return { ...state, items: [...state.items].filter(item => item.id !== action.id) };
    }
    case CANCEL_PROMO: {
      return {
        ...state,
        promoCode: '',
        promoDiscount: null
      };
    }
    default: {
      return state;
    }
  }
};
