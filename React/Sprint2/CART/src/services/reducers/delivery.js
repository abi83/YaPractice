import {
  GET_DELIVERY_METHODS,
  GET_DELIVERY_METHODS_FAILED,
  SET_DELIVERY_METHOD,
  GET_DELIVERY_METHODS_SUCCESS
} from '../actions/delivery';

const deliveryInitialState = {
  deliveryMethods: [],
  deliveryMethodsRequest: false,
  deliveryMethodsFailed: false,
  selectedDeliveryId: null
};
export const deliveryReducer = (state = deliveryInitialState, action) => {
  switch (action.type) {
    case GET_DELIVERY_METHODS: {
      return {
        ...state,
        deliveryMethodsFailed: false,
        deliveryMethodsRequest: true
      };
    }
    case GET_DELIVERY_METHODS_FAILED: {
      return {
        ...state,
        deliveryMethodsFailed: true,
        deliveryMethodsRequest: false
      };
    }
    case GET_DELIVERY_METHODS_SUCCESS: {
      return {
        ...state,
        deliveryMethods: action.methods,
        deliveryMethodsRequest: false,
        selectedDeliveryId:
          !!action.methods.length && state.selectedDeliveryId === null
            ? action.methods[0].id
            : state.selectedDeliveryId
      };
    }
    case SET_DELIVERY_METHOD: {
      return {
        ...state,
        selectedDeliveryId: action.id
      };
    }
    default: {
      return state;
    }
  }
};
