import axios from "axios";

import {
	USER_INFORMATION_URL,
	USER_SERVERS_URL,
	USER_SERVER_CHANNELS_URL,
	USER_STATISTICS_URL,
} from "../Utils/constants";

export const getUserInformationService = async (token) => {
	try {
		const { data } = await axios.get(USER_INFORMATION_URL, { headers: { Authorization: `token ${token}` } });

		return data;
	} catch (err) {
		throw err.response.data;
	}
};

export const getUserServersService = async (token) => {
	try {
		const { data } = await axios.get(USER_SERVERS_URL, { headers: { Authorization: `token ${token}` } });

		return data;
	} catch (err) {
		throw err.response.data;
	}
};

export const getServerChannelsService = async (token, serverId) => {
	try {
		const { data } = await axios.get(`${USER_SERVER_CHANNELS_URL}/${serverId}`, {
			headers: { Authorization: `token ${token}` },
		});

		return data;
	} catch (err) {
		throw err.response.data;
	}
};

export const getStatisticsService = async (token) => {
	try {
		console.log(token);
		const { data } = await axios.get(USER_STATISTICS_URL, { headers: { Authorization: `token ${token}` } });

		return data;
	} catch (err) {
		throw err.response.data;
	}
};
