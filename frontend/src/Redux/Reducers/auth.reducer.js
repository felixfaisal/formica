import { LOGIN, LOGOUT } from "../ActionTypes";

const initialState = {
	isLoggedIn: false,
	token: null,
};

export const auth = (state = initialState, action) => {
	switch (action.type) {
		case LOGIN: {
			return {
				...state,
				isLoggedIn: true,
				token: action.payload.token,
			};
		}
		case LOGOUT: {
			return initialState;
		}
		default:
			return state;
	}
};
