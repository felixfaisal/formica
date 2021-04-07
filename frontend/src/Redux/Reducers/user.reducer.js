import { GET_USER_INFORMATION, GET_USER_SERVERS, LOGOUT } from "../ActionTypes";

const initialState = {
	userId: null,
	name: null,
	avatar: null,
	servers: [],
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
		case GET_USER_SERVERS: {
			return {
				...state,
				servers: action.payload.servers,
			};
		}
		case LOGOUT: {
			return initialState;
		}
		default:
			return state;
	}
};
