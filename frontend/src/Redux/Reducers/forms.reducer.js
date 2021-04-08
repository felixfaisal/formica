import { GET_FORMS } from "../ActionTypes";

const initialState = {
	forms: [],
};

export const forms = (state = initialState, action) => {
	switch (action.type) {
		case GET_FORMS: {
			return {
				...state,
				forms: action.payload.forms,
			};
		}
		default:
			return state;
	}
};
