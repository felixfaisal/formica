import React, { useEffect, useState } from "react";
import { useSelector } from "react-redux";

import StatisticsCard from "../../Components/StatisticsCard/StatisticsCard";
import Toast from "../../Components/Toast";

import { getStatisticsService } from "../../Services/users.service";

import styles from "./Dashboard.module.css";

const Dashboard = () => {
	const [loading, setLoading] = useState(true);
	const [statistics, setStatistics] = useState([]);
	const { token } = useSelector((state) => state.auth);

	useEffect(() => {
		fetchStatistics();
	}, []);

	const fetchStatistics = async () => {
		try {
			const data = await getStatisticsService(token);
			setStatistics(Object.keys(data).map((key) => ({ title: key, body: data[key] })));
			setLoading(false);
		} catch (err) {
			Toast("Some error has occurred!", "error");
		}
	};

	const displayStatistics = statistics.map((statistic) => (
		<StatisticsCard title={statistic.title} body={statistic.body} />
	));

	return loading ? (
		<div className={styles.container}>
			<h3 className={styles.subtitle}>Please Wait...</h3>
		</div>
	) : (
		<div className={styles.container}>{displayStatistics}</div>
	);
};

export default Dashboard;
