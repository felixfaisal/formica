import { getUserInformationService } from "../../Services/users.service";
import { GET_USER_INFORMATION, LOGIN } from "../ActionTypes";

export const getUserInformation = (token) => async (dispatch, getState) => {
	try {
		const userData = await getUserInformationService(token);
		console.log(userData);

		dispatch({
			type: GET_USER_INFORMATION,
			payload: { name: userData.tag.split("#")[0], avatar: userData.avatar },
		});
		dispatch({
			type: LOGIN,
			payload: { token },
		});
	} catch (err) {
		throw err;
	}
};
