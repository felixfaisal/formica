import { createFormService, getFormsService } from "../../Services/forms.service";
import { GET_FORMS } from "../ActionTypes";

export const createForm = (formData) => async (_, getState) => {
	try {
		const {
			auth: { token },
		} = getState();

		const response = await createFormService(token, formData);

		return response;
	} catch (err) {
		throw err;
	}
};

export const getForms = () => async (dispatch, getState) => {
	try {
		const {
			auth: { token },
		} = getState();

		const forms = await getFormsService(token);

		dispatch({ type: GET_FORMS, payload: { forms } });
	} catch (err) {
		throw err;
	}
};
