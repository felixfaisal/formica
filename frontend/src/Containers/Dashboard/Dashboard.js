import React from "react";

import StatisticsCard from "../../Components/StatisticsCard/StatisticsCard";

import styles from "./Dashboard.module.css";

import statistics from "../../Assets/Data/statistics";

const Dashboard = () => {
	const displayStatistics = statistics.map((statistic) => (
		<StatisticsCard title={statistic.title} body={statistic.body} />
	));

	return <div className={styles.container}>{displayStatistics}</div>;
};

export default Dashboard;
