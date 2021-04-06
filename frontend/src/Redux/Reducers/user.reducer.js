import { GET_USER_INFORMATION } from "../ActionTypes";

export const user = (
	state = {
		name: null,
		avatar: null,
	},
	action
) => {
	switch (action.type) {
		case GET_USER_INFORMATION: {
			return {
				...state,
				name: action.payload.name,
				avatar: action.payload.avatar,
			};
		}
		default:
			return state;
	}
};
