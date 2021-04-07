import { createFormService } from "../../Services/forms.service";

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
