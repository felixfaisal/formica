import React from "react";

import styles from "./StatisticsCard.module.css";

const StatisticsCard = ({ title, body }) => {
	return (
		<div className={styles.card_container}>
			<h2 className={styles.card_title}>{title}</h2>
			<h3 className={styles.card_body}>{body}</h3>
		</div>
	);
};

export default StatisticsCard;
