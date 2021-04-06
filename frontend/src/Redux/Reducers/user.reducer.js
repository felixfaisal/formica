import { GET_USER_INFORMATION, LOGOUT } from "../ActionTypes";

const initialState = {
	userId: null,
	name: null,
	avatar: null,
};

export const user = (state = initialState, action) => {
	switch (action.type) {
		case GET_USER_INFORMATION: {
			return {
				...state,
				userId: action.payload.userId,
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
