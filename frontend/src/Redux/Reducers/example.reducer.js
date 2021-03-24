import { EXAMPLE_ACTION } from "../ActionTypes";

export const example = (
  state = {
    exampleState: 1,
  },
  action
) => {
  switch (action.type) {
    case EXAMPLE_ACTION: {
      return {
        ...state,
        exampleState: state.exampleState + 1,
      };
    }
    default:
      return state;
  }
};