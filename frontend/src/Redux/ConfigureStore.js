import { createStore, combineReducers, applyMiddleware } from "redux";
import thunk from "redux-thunk";
import { persistStore, persistCombineReducers } from "redux-persist";
import storage from "redux-persist/lib/storage";

import { example } from "./Reducers/example.reducer";
import { auth } from "./Reducers/auth.reducer";
import { user } from "./Reducers/user.reducer";
import { forms } from "./Reducers/forms.reducer";

const config = {
	key: "root",
	storage: storage,
};

export const ConfigureStore = () => {
	const store = createStore(persistCombineReducers(config, { example, auth, user, forms }), applyMiddleware(thunk));
	const persistor = persistStore(store);

	return { store, persistor };
};
