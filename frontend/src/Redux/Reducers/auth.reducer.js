import { LOGIN } from "../ActionTypes";

export const auth = (
	state = {
		isLoggedIn: false,
	},
	action
) => {
	switch (action.type) {
		case LOGIN: {
			return {
				...state,
				isLoggedIn: true,
				token: action.payload.token,
			};
		}
		default:
			return state;
	}
};
