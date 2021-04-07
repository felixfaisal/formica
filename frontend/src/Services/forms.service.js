import axios from "axios";
import { CREATE_FORMS_URL, GET_FORMS_URL } from "../Utils/constants";

export const createFormService = async (token, formData) => {
	try {
		const { data } = await axios.post(CREATE_FORMS_URL, formData, { headers: { Authorization: `token ${token}` } });

		return data;
	} catch (err) {
		throw err.response.data;
	}
};

export const getFormsService = async (token) => {
	try {
		const { data } = await axios.get(GET_FORMS_URL, { headers: { Authorization: `token ${token}` } });

		return data;
	} catch (err) {
		throw err.response.data;
	}
};
