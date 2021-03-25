import { createStore, combineReducers } from "redux";

import { example } from "./Reducers/example.reducer";
import { auth } from "./Reducers/auth.reducer";

export const ConfigureStore = () => {
	const store = createStore(combineReducers({ example, auth }));

	return store;
};
