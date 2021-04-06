import { GET_USER_INFORMATION, LOGOUT } from "../ActionTypes";

const initialState = {
	name: null,
	avatar: null,
};

export const user = (state = initialState, action) => {
	switch (action.type) {
		case GET_USER_INFORMATION: {
			return {
				...state,
				name: action.payload.name,
				avatar: action.payload.avatar,
			};
		}
		case LOGOUT: {
			return initialState;
		}
		default:
			return state;
	}
};
