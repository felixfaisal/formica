import { createStore, combineReducers } from "redux";

import { example } from "./Reducers/example.reducer";

export const ConfigureStore = () => {
  const store = createStore(
    combineReducers({ example }),
  );

  return store;
};