import React from "react";
import { useParams } from "react-router";

import styles from "./FormResponses.module.css";

const FormResponses = ({ responses }) => {
	const displayHeadings = responses[0] ? (
		Object.keys(responses[0]).map((key) => <div className={styles.heading}>{key}</div>)
	) : (
		<h3 className={styles.heading}>No Responses Yet!</h3>
	);

	const displayRow = (row) => Object.keys(row).map((key) => <div className={styles.data}>{row[key]}</div>);

	const displayRows = responses.map((row) => <div className={styles.row}>{displayRow(row)}</div>);

	return (
		<div className={styles.container}>
			<div className={styles.row}>{displayHeadings}</div>
			{displayRows}
		</div>
	);
};

export default FormResponses;
