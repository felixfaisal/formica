import { getUserInformationService, getUserServersService } from "../../Services/users.service";
import { GET_USER_INFORMATION, GET_USER_SERVERS, LOGIN } from "../ActionTypes";

export const getUserInformation = (token) => async (dispatch) => {
	try {
		const userData = await getUserInformationService(token);

		dispatch({
			type: GET_USER_INFORMATION,
			payload: { name: userData.tag.split("#")[0], avatar: userData.avatar, userId: userData.userid },
		});
		dispatch({
			type: LOGIN,
			payload: { token },
		});
	} catch (err) {
		throw err;
	}
};

export const getUserServers = () => async (dispatch, getState) => {
	try {
		const {
			auth: { token },
		} = getState();

		const servers = await getUserServersService(token);

		dispatch({
			type: GET_USER_SERVERS,
			payload: { servers: servers.filter((server) => server.permissions_new[0] === "8" || server.owner === true) },
		});
	} catch (err) {
		throw err;
	}
};
